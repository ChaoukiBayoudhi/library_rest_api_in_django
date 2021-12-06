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
#syntax : nomModele.objects.Method([parameters])
# Method peut être all(), get(), filter(), exclude(),....
#Au lieu de method on peut avoir une chaine de méthodes
#par exemple .filter(...).filter(....).exclude(....)
#en SQL : select * from Book
#avec l'ORM :
#Le resultat est l'objet QuerySet
# result=Book.objects.all()
#recupere le book dont le title est x
#result=Book.objects.get(title=x)
#recupere les books telsque la date de sortie est après 2010
#books=Book.objects.filter(releaseDate__year__gt=2010)
#au lieu de __gt on peut avoir __lt(<), __gte(>=),__lte
#__exact, __iexact (insensitive exact)
#__contains, icontains, __isnull, __startwith,__endswith,...
#ordonner le resultat par title
#result=Book.objects.order_by('title')

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

@api_view(['POST'])
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
    # if request.method == 'GET':
    #     return getAllBooks(request)
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
            return Response(status=status.HTTP_202_ACCEPTED)
    return Response(bookSerialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['PUT','PATCH'])
def updateAuthor(request,pk):
    
    if request.method=='PUT':
        pass
    elif request.method=='PATCH':
        pass
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



