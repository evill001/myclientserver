from django.contrib import admin
from django.urls import path
from myapp.views import BooksList, BooksDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BooksList.as_view(), name='books-detail'),
    path('books/<int:pk>/', BooksDetail.as_view(),name='bools=detail'),
]
