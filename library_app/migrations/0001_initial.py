# Generated by Django 3.2.8 on 2021-11-24 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lasrName', models.CharField(max_length=20)),
                ('birthDate', models.DateField(default=datetime.date(1980, 11, 1))),
                ('photo', models.ImageField(max_length=200, upload_to='photos/authors')),
            ],
            options={
                'verbose_name': 'Ahothor',
                'verbose_name_plural': 'Authors',
                'db_table': 'author_tab',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('esbnCode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('releaseDate', models.DateField(default=datetime.date(2000, 1, 1))),
                ('summarize', models.TextField(max_length=300)),
                ('cover', models.ImageField(max_length=254, upload_to='photos/books')),
                ('authors_books', models.ManyToManyField(to='library_app.Author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book_tab',
                'managed': True,
            },
        ),
    ]
