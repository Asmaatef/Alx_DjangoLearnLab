from django.contrib import admin
from .models import Author, Book, Library, Librarian

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

from relationship_app.query_samples import get_books_by_author, get_books_in_library, get_librarian_for_library

# Replace with actual values after creating instances
get_books_by_author('Author ')
get_books_in_library('Library ')
get_librarian_for_library('Librarian')