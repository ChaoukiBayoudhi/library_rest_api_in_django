# Generated by Django 3.2.8 on 2021-12-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_book_booktype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors_books',
            field=models.ManyToManyField(blank=True, null=True, to='library_app.Author'),
        ),
    ]
