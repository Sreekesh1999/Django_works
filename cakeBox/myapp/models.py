from django.db import models

# Create your models here.
class Cakes(models.Model):
    name=models.CharField(max_length=100)
    flavour=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    shape=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    layer=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=300)
    date=models.DateTimeField(auto_now_add=True)
    photo=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name
