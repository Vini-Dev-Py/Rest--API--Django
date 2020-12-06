from rest_framework import viewsets
from books.api import serializers
from books import models

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializes
    queryset = models.Books.objects.all()