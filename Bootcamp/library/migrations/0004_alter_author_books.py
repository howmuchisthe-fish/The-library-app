# Generated by Django 5.0.7 on 2024-08-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_author_name_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='library.book'),
        ),
    ]
