from .models import Book
from django.forms.models import model_to_dict
from django.core.cache import cache
from .logging import logger

def seed_cache():
    books = Book.objects.all()
    book_data = { book.id : model_to_dict(book) for book in books}
    for id, book in book_data.items():
        book["id"] = id
        logger.info(book)
        cache.set(f"book:{id}", book, timeout=86400)
    
    