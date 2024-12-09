from django.urls import path
from .views import BookList
generics.ListAPIView 
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Book

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
