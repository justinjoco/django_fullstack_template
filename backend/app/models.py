from django.db import models
import uuid
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    title = models.TextField(null=False)
    author = models.TextField(null = False)
    genre = models.TextField(null = False)
    description = models.TextField(null = True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    date_published = models.DateTimeField(null = True)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = "book"