from django.db.models import fields
from rest_framework import serializers
from .models import Author,Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta :
        model = Author
        fields=('firstName','lastName','birthDate','photo')
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, many=True)
    class Meta :
        model = Book
        # fields=('esbnCode','title','releaseDate','summarize','author')
        fields='__all__'