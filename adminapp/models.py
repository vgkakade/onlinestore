from django.db import models
from django.urls import reverse

# Create your models here.
book_type = [
    ('Hardback', 'HardBack'),
    ('Paperback', 'Paperback'),
]
languages_available = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Marathi', 'Marathi'),
]

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=512)
    author = models.CharField(max_length=256)
    ISBN = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField()
    language = models.CharField(max_length=256, choices=languages_available)
    type = models.CharField(max_length=256, choices=book_type)
    price = models.PositiveIntegerField()
    genre = models.CharField(max_length=256)
    published_year = models.PositiveIntegerField()
    description = models.TextField(max_length=350)
    thumb = models.ImageField(default='products/default.png', blank=True, upload_to='products')  # blank field is also allowed

    class Meta:
        db_table = "tblbooks"

    def __str__(self):
        return self.name

class tblAdmin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'tbladmin'

    def __str__(self):
        return self.username