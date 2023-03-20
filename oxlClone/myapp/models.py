from django.db import models

# Create your models here.
class Vehicles(models.Model):
    name=models.CharField(max_length=250)
    model=models.CharField(max_length=200)
    category=models.CharField(max_length=230)
    owner_type=models.CharField(max_length=200)
    fuel_type=models.CharField(max_length=200)
    kms=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=2550)
    number=models.CharField(max_length=200,unique=True)

class Mobiles(models.Model):
    name=models.CharField(max_length=250)
    brand=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    display=models.CharField(max_length=100,default="lcd")

    def __str__(self):
        return self.name
    
#Movies
#name,genres,year,language,rating
# #

class Movies(models.Model):
    name=models.CharField(max_length=250,unique=True)
    genre=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    language=models.CharField(max_length=100)
    rating=models.FloatField()

    def __str__(self):
        return self.name
