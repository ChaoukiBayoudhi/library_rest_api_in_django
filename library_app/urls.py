from django.urls import include, path
from rest_framework import routers

from .views import AuthorViewSet, BookViewSet
from .views import getAllAuthors,getBookByNameLike,addAuthor,addBook,deleteAuthor,deleteBook,updateAuthor,updateBook,getAllBooks

router=routers.DefaultRouter()
#if "r" or "R" prefix is present escape sequences (like \n, \a,\t,",',\,...)
#are not interpreted and they'll be shown as they are written
router.register(r'author',AuthorViewSet)
router.register(r'book',BookViewSet)




urlpatterns = [
    path('',include(router.urls)),
    path(r'authors/all/',getAllAuthors,name='allAuthor'),
    path(r'authors/add/',addAuthor,name="addAuthor"),
    path(r'authors/delete/<int:pk>',deleteAuthor,name="deleteAuthor"),
    path(r'authors/update/<int:pk>',updateAuthor,name="updateAuthor"),
    path(r'books/add/',addBook,name="addBook"),
    path(r'books/all/',getAllBooks,name='allBooks'),
    path(r'books/delete/<str:pk>',deleteBook,name='deleteBook'),
    path(r'books/update/<str:pk>',updateBook,name='updateBook'),
    path(r'books/title-like/<str:title>',getBookByNameLike,name='bookTitleLike')
]
