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

@api_view(['POST'])
def author(request):
    if request.method == 'POST':
        author = AuthorSerializer(data=request.data)
        if author.is_valid():
            author.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(author.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_200_OK)

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
def getBookByNameLike(request, expression):
    if request.method=='GET':
        books=Book.objects.filter(title__icontains=expression)
        if books.is_empty():
            return Response(status=status.HTTP_404_NOT_FOUND)
        result=BookSerializer(books,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT','PATCH'])
def updateBook(request,pk):
    if request.method=='PUT':
        pass
    elif request.method=='PATCH':
        pass
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



