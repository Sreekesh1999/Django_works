# Generated by Django 4.1.7 on 2023-03-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_movies_name_alter_movies_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]