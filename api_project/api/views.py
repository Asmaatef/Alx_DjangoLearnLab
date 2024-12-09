from django.urls import path
from .views import BookList
generics.ListAPIView 
from .serializers import BookSerializer
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
