from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BooksSerializer


class BooksList(generics.ListCreateAPIView):  # GET
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksDetail(generics.RetrieveUpdateDestroyAPIView):  # POST, PUT, DELETE
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
