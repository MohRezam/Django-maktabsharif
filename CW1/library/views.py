from django.shortcuts import render
from library.models import Book, Author, Member
# Create your views here.
def home(request):
    if request.method == "GET":
        book = Book.objects.all()
        author = Author.objects.all()
        member = Member.objects.all()
        return render(request, "index.html", context={"book":book, "author": author, "member":member})
    