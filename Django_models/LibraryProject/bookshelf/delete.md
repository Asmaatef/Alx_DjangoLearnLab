book.delete()
books = Book.objects.all()
for b in books:
    print(b)
