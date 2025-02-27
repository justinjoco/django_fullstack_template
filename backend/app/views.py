from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import JsonResponse
from django.core.cache import cache
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, partial=True, **kwargs)  # Always allow partial updates
    
def health_check(request):
    cache.set("ping", "pong", timeout=1)
    value = cache.get("ping")
    return JsonResponse({"ping": value}, status=200)