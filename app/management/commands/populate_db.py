from django.core.management.base import BaseCommand
from app.models import Author, Book, Stock


class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        # Create authors
        author1 = Author.objects.create(first_name='John', last_name='Doe', bio='Sample bio 1')
        author2 = Author.objects.create(first_name='Jane', last_name='Doe', bio='Sample bio 2')
        author3 = Author.objects.create(first_name='Jim', last_name='Doe', bio='Sample bio 3')

        # Create books
        book1 = Book.objects.create(title='Book 1', publish_date='2021-01-01')
        book1.authors.add(author1)
        book2 = Book.objects.create(title='Book 2', publish_date='1972-01-01')
        book2.authors.add(author1)
        book3 = Book.objects.create(title='Book 3', publish_date='1994-01-01')
        book3.authors.add(author2)
        book4 = Book.objects.create(title='Book 4', publish_date='1982-05-24')
        book4.authors.add(author2)
        book5 = Book.objects.create(title='Book 5', publish_date='2000-12-31')
        book5.authors.add(author3)

        # Create stock items
        Stock.objects.create(book=book1, price_excl_vat=24.33, vat_percentage=10, discount=5.00)
        Stock.objects.create(book=book2, price_excl_vat=16.92, vat_percentage=10, discount=0)
        Stock.objects.create(book=book3, price_excl_vat=14.22, vat_percentage=10, discount=2.50)
        Stock.objects.create(book=book4, price_excl_vat=7.00, vat_percentage=10, discount=0)