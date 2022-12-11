from rest_framework import generics, viewsets, filters
from django.shortcuts import render
from rest_framework.response import Response

from .models import *
from .permissions import IsAdminOrReadOnly
from .serializers import *


def index(request):
    return render(request, 'index.html')


class BookAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "author__middle_name", "genre"]
    permission_classes = [IsAdminOrReadOnly]


class AuthorAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [IsAdminOrReadOnly]


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        item = BooksSerializer(data=request.data)

        if Book.objects.filter(publisher=request.data.get('publisher'),
                               author=request.data.get('author'),
                               title=request.data.get('title'),
                               yearOfRel=request.data.get(
                                   'yearOfRel')).exists() and ', переведенное с другого языка' \
                in request.data.get('genre'):
            raise serializers.ValidationError('У данного издательства есть перевод этого хужожественного произведения')

        if Book.objects.filter(publisher=request.data.get('publisher'),
                               author=request.data.get('author'),
                               title=request.data.get('title'),
                               yearOfRel=request.data.get(
                                   'yearOfRel')).exists() and ', переиздание' in request.data.get('genre'):
            raise serializers.ValidationError('Учебник этого издания существует')

        if item.is_valid():
            item.save()
            return Response('Книга успешно добавлена')
        else:
            return Response('Книга не добавлена')
