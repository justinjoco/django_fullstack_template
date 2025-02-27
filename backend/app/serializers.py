from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required = False, allow_blank = True, allow_null = True)
    rating = serializers.DecimalField(max_digits=10, decimal_places=2, required = False)
    date_published = serializers.DateTimeField(required = False)

    class Meta:
        model = Book
        fields = "__all__"
