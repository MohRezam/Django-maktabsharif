from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    ISBN = models.IntegerField()
    borrowed_date = models.DateTimeField() 
    return_date = models.DateTimeField()
    availability = True
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    biography = models.TextField()
    book = models.ManyToManyField(Book)
    
class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.IntegerField()
    book = models.ManyToManyField(Book)
    