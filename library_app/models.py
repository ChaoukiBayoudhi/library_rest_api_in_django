from datetime import date
from django.db import models
from django.utils.dateparse import parse_date
#from django.utils.dateparse import parse_datetime #for dateime
from django.utils.timezone import now


# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    birthDate=models.DateField(default=date(1980,11,1))
    photo = models.ImageField(upload_to='photos/authors', max_length=200)
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
    cover=models.ImageField(upload_to="photos/books",max_length=254)
    authors_books=models.ManyToManyField(Author)
    class Meta:
        db_table = 'book_tab'
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'