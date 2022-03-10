from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    return render(request, 'index.html')


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})
