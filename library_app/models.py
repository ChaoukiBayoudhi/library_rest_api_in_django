from datetime import date
from django.db import models
from django.db.models import fields
from django.utils.dateparse import parse_date
from django import forms
#from django.utils.dateparse import parse_datetime #for dateime


# Create your models here.
BookTypes=[
        ('literature','LITERATURE'),
        ('scientific','SCIENTIFIC'),
        ('humanity','HUMANITY'),
        ('other','OTHER')
    ]
class Author(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    birthDate=models.DateField(default=date(1980,11,1))
    photo = models.ImageField(upload_to='photos/authors', max_length=200,null=True,blank=True)
    class Meta:
        db_table = 'author_tab'
        managed = True #default value
        verbose_name = 'Ahothor'
        verbose_name_plural = 'Authors'
        
class Book(models.Model):
    esbnCode=models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=20)
    releaseDate=models.DateField(default=parse_date('2000-01-01'))
    summarize=models.TextField(max_length=300)
    cover=models.ImageField(upload_to="photos/books",max_length=254, null=True,blank=True)
    authors_books=models.ManyToManyField(Author,null=True,blank=True)
    bookType=models.CharField(max_length=10,null=True,blank=True,choices=BookTypes)
    class Meta:
        db_table = 'book_tab'
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


#form Classes
class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['firstName','lastName','birthDate','photo']

#en HTML en utilise les balises HTML et L DTL : Django Template Language :
#si on veut recuperer la valeur d'une variable
#{{ nom_variable }}
#{%for x in books :}
# <tr>
     #<td>{{ x.title }}
     #....
#{% endfor %}
#{%if condition :%}
#....
#{% endif %}

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

#the previous code is equivalent to the below one
# class BookForm(forms.Form):
#     esbnCode=forms.CharField(max_length=20)
#     title = forms.CharField(max_length=10)
#     releaseDate = forms.DateField(required=False)
#     bookType = forms.CharField(
#     max_length=10,
#     widget=forms.Select(choices=BookTypes),
#     )
