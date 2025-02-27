from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView, health_check

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List of books
    path('book', BookCreateView.as_view(), name='book-create'),  # Create book
    path('book/<uuid:pk>', BookDetailView.as_view(), name='book-detail'),  # Single book actions
    path('health_check', health_check, name="health-check")
]