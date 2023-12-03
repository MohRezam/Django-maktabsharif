from django.contrib import admin
from library.models import Book, Author, Member

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Member)
