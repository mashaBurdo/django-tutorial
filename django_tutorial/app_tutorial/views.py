from django.http import HttpResponse
from django.shortcuts import render

from .models import Book, Review


def index(request):
    return render(request, 'index.html')


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', {'review': review})