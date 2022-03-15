from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book_list/', views.book_list, name='book_list'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
]