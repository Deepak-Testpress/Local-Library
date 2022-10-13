from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    genres = Genre.objects.count()

    code_books = Book.objects.filter(title__contains='code')
    number_code_books = code_books.count()


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    	'genres':genres,
        'number_code_books':number_code_books,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

