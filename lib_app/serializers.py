from rest_framework import serializers

from . import models


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'
