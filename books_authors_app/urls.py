from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add_book', views.add_book),
    path('book/<int:book_id>', views.book),
    path('book/<int:book_id>/edit_book', views.edit_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('author/<int:author_id>', views.author),
    path('author/<int:author_id>/edit_author', views.edit_author)
]
