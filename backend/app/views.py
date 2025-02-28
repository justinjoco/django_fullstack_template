from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.core.cache import cache
from rest_framework.response import Response
from .logging import logger
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        cached_keys = cache.keys("book:*")
        if len(cached_keys) > 0:
            return Response(cache.get_many(cached_keys).values())
    
        return super().list(request, *args, **kwargs)

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        cache.set(f"book:{instance.id}", serializer.data, timeout = 3600)
        return instance

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        id = self.kwargs[self.lookup_field]
        cache_key = f"book:{id}"
        cached_data = cache.get(cache_key)

        return Response(cached_data) if cached_data else super().get(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Optionally, you can override this to perform additional logic
        instance = self.get_object()  # Get the object to be updated
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Use partial=True for PATCH requests
        
        # Validate the data before updating
        if serializer.is_valid():
            # Call `perform_update()` after validation
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    def perform_update(self, serializer):
        instance = serializer.save()
        cache.set(f"book:{instance.id}", serializer.data, timeout = 3600)

    def perform_destroy(self, instance):
        cache.delete(f"book:{instance.id}")
        logger.info(f"ID to delete: book:{instance.id}")
        instance.delete()
    
