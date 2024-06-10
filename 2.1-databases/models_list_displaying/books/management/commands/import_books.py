import csv

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('books.csv', 'r') as file:
            books = list(csv.DictReader(file, delimiter=';'))

        for book in books:
            ph = Book(name=book['name'], author=book['author'], pub_date=book['pub_date'])
            ph.save()