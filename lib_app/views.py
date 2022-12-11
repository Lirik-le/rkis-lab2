from rest_framework import generics, viewsets, filters
from django.shortcuts import render

from .models import *
from .permissions import IsAdminOrReadOnly
from .serializers import *


def index(request):
    return render(request, 'index.html')


class BookAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author", "genre"]

