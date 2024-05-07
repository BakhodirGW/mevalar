from django.db.models.deletion import SET_NULL
from django.db import models


class Notification(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    sab_code = models.FloatField()
    image = models.ImageField(upload_to='mahsulot/')

    def __str__(self):
        return self.title


