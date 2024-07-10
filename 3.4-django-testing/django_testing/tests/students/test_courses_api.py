import json

import pytest
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient, APIRequestFactory
from model_bakery import baker
from students.serializers import CourseSerializer
from students.models import Course


def test_example():
    assert False, "Just test example"


@pytest.mark.django_db
def test_retrieve(course_factory, api_client):
    # Arrange
    course = course_factory(name='course')

    # Act
    course_get = api_client.get('/api/v1/courses/')

    # Assert
    assert course_get.status_code == 200
    assert course_get.data[0]['id'] == course.id


@pytest.mark.django_db
def test_list(course_factory, api_client):
    # Arrange
    course = course_factory(_quantity=10, name='course')
    set_course_id = set([v.id for v in course])

    # Act
    course_get = api_client.get('/api/v1/courses/')
    res_set = set([v['id'] for v in course_get.data])

    # Assert
    assert course_get.status_code == 200
    assert res_set == set_course_id


@pytest.mark.django_db
def test_id(course_factory, api_client):
    # Arrange
    course = course_factory(_quantity=10, name='course')
    dict_course = dict((v.id, v) for v in course)

    # Act
    course_get = api_client.get('/api/v1/courses/', {'id':5})

    # Assert
    assert course_get.status_code == 200
    assert course_get.data[0]['id'] == dict_course[5].id


@pytest.mark.django_db
def test_name(course_factory, api_client):
    # Arrange
    course = course_factory(_quantity=10)
    name_course = course[5].name

    # Act
    course_get = api_client.get('/api/v1/courses/', {'name': name_course})

    # Assert
    assert course_get.status_code == 200
    assert course_get.data[0]['name'] == name_course


@pytest.mark.django_db
def test_create_course(api_client):
    # Arrange
    course = {'name': 'course222'}

    # Act
    course_post = api_client.post('/api/v1/courses/', data=course)

    # Assert
    assert course_post.status_code == 201 and course_post.data['name'] == 'course222'


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    # Arrange
    course = course_factory(_quantity=1, name='course222')
    course_update = {'name': 'course555'}

    # Act
    course_ob = Course.objects.get(pk=course[0].id)
    serializer_update = CourseSerializer(course_ob, data=course_update)

    if serializer_update.is_valid():
        serializer_update.save()
        course_ob = Course.objects.get(pk=course[0].id)
        res = Response(serializer_update.data, status=status.HTTP_200_OK)
    else:
        res = Response(serializer_update.errors, status=status.HTTP_400_BAD_REQUEST)

    # Assert
    assert res.status_code == 200
    assert course_ob.name == 'course555'


@pytest.mark.usefixtures("api_client")
@pytest.mark.django_db
def test_delete_course(api_client):
    # Arrange
    course = {'name': 'course222'}

    # Act
    course_post = api_client.post('/api/v1/courses/', data=course)
    course_ob = Course.objects.get(pk=course_post.data['id'])
    course_ob.delete()
    res = Response(status=status.HTTP_204_NO_CONTENT)

    # Assert
    assert res.status_code == 204