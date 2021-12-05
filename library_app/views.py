from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    http_method_names=['get','post','delete','put']






    #2ème méthode

@api_view(['GET'])
def getAllBooks(request):
    if request.method=='GET':
        if Book.objects.count()==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        books=Book.objects.all()
        result=BookSerializer(books,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def getAllAuthors(request):
    if request.method=='GET':
        if Author.objects.count()==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        authors=Author.objects.all()
        result=AuthorSerializer(authors,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def getBookByNameLike(request, title):
    if request.method=='GET':
        books=Book.objects.filter(title__icontains=title)
        if not books.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        result=BookSerializer(books,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','POST'])
def addBook(request):
    
    if request.method=='POST':
        book=BookSerializer(data=request.data)
        if not book.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        b1 = Book.objects.get(pk=book.pk)
        if b1.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        book.save()
        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        return getAllBooks(request)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','POST'])
def addAuthor(request):
    if request.method == 'POST':
        author = AuthorSerializer(data=request.data)
        if author.is_valid():
            author.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(author.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        return getAllAuthors(request)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def deleteAuthor(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
def getBookByPk(pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return book
@api_view(['DELETE'])
def deleteBook(request, pk):
    book=getBookByPk(pk)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    
@api_view(['PUT','PATCH'])
def updateBook(request,pk):
    book=getBookByPk(pk)
    if request.method=='PUT':
        bookSerialized = BookSerializer(book,request.data)
    elif request.method=='PATCH':
        bookSerialized = BookSerializer(book,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if bookSerialized.is_valid():
            bookSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(bookSerialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['PUT','PATCH'])
def updateAuthor(request,pk):
    
    if request.method=='PUT':
        pass
    elif request.method=='PATCH':
        pass
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



