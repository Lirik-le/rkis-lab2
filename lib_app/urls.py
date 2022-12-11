from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CreateBook

urlpatterns = [
    path('book_list', views.BookAPIView.as_view({'get': 'list'})),
    path('book_create', CreateBook.as_view()),
    path('book_detail/<int:pk>', views.BookAPIView.as_view({'get': 'retrieve'})),
    path('book_update/<int:pk>', views.BookAPIView.as_view({'post': 'update'})),
    path('book_delete/<int:pk>', views.BookAPIView.as_view({'get': 'destroy'})),
    path('author_list', views.AuthorAPIView.as_view({'get': 'list'})),
    path('author_create', views.AuthorAPIView.as_view({'post': 'create'})),
    path('author_detail/<int:pk>', views.AuthorAPIView.as_view({'get': 'retrieve'})),
    path('author_update/<int:pk>', views.AuthorAPIView.as_view({'post': 'update'})),
    path('author_delete/<int:pk>', views.AuthorAPIView.as_view({'get': 'destroy'})),
]

