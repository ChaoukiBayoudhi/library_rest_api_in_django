# Generated by Django 3.2.8 on 2021-11-25 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='lasrName',
            new_name='lastName',
        ),
    ]