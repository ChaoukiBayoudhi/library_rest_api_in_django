from django.urls import include, path
from rest_framework import routers


from .views import AuthorViewSet, BookViewSet, author, author_detail

router=routers.DefaultRouter()
#if "r" or "R" prefix is present escape sequences (like \n, \a,\t,",',\,...)
#are not interpreted and they'll be shown as they are written
router.register(r'author',AuthorViewSet)
router.register(r'book',BookViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('allauthors/',author,name='allauthor'),
    path('author/<int:pk>/',author_detail,name='AuthDetail'),
]
