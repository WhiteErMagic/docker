import django_filters
from django_filters import rest_framework as filters, DateFromToRangeFilter, CharFilter, NumberFilter
from rest_framework import request
from rest_framework.authtoken.admin import User

from .models import Advertisement
from django.conf import settings


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()
    status = CharFilter()
    creator = NumberFilter(field_name='creator_id')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']