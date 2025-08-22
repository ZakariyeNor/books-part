from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# List all books or create a new book
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve, update, or delete a single book
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer