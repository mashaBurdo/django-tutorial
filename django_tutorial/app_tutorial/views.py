from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookForm, LoginForm, RegisterForm
from .models import Book, Review


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book.objects.create(**form.cleaned_data)
            return redirect('book_detail', book.id)
    else:
        form = BookForm()
        return render(request, 'book_form.html', {'form': form})


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


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


def book_review_list(request, book_id):
    reviews = Review.objects.filter(book=book_id)
    return render(request, 'review_list.html', {'reviews': reviews})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login_form.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponse('Logged out')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            print(form.errors)
        return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()

        return render(request, "register_form.html", {"form": form})