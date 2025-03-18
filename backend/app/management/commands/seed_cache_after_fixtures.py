from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core.cache import cache
from app.logging import logger
from django.forms.models import model_to_dict

class Command(BaseCommand):
    help = "Load fixtures and seed the cache afterward"

    def handle(self, *args, **kwargs):
        # Load fixtures first (if you have them in your app)
        call_command('loaddata', 'app/fixtures/books.json')

        # Now, seed the cache after the fixtures are loaded
        self.seed_cache()

    def seed_cache(self):
        # This method will populate the cache
        from app.models import Book

        books = Book.objects.all()
        book_data = { book.id : model_to_dict(book) for book in books}
        for id, book in book_data.items():
            book["id"] = id
            logger.info(book)
            cache.set(f"book:{id}", book, timeout=86400)
    