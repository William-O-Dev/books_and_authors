from django.shortcuts import render, redirect
from .models import Book, Author

def home(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request,'home.html', context)

def add_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        )
    return redirect('/')

def book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'authors': Author.objects.exclude(books__id=book_id)
    }
    return render(request,'book.html', context)

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    book.save()    
    return redirect(f'/book/{book_id}')

def authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request,'authors.html', context)

def add_author(request):
        Author.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notes = request.POST['notes'],
            )
        return render(request,'authors.html')

def author(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'books': Book.objects.exclude(authors__id=author_id)
    }
    return render(request, 'author.html', context)

def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    author.save()
    return redirect(f'/author/{author_id}')
