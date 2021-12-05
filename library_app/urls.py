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
    path('authors/all/',getAllAuthors,name='allAuthor'),
    path('authors/delete/<int:pk>/',deleteAuthor,name='DeleteAuthor'),
    path('authors/add/',addAuthor,name="addAuthor"),
    path('authors/delete/',deleteAuthor,name="deleteAuthor"),
    path('authors/update/',updateAuthor,name="updateAuthor"),
    path('books/add/',addBook,name="addBook"),
    path('books/all/',getAllBooks,name='allBooks'),
    path('books/delete/',deleteBook,name='deleteBook'),
    path('books/update/',updateBook,name='updateBook'),
    path('books/title-like/<str:title>',getBookByNameLike,name='bookTitleLike')
]
