from django.db import models

# Create your models here.


class User(models.Model): #This create a 'User' table in the database
    user_id = models.BigAutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255) # name, VARCHAR(255)
    age= models.PositiveIntegerField(null=True)


#Creating the model(schema for the database) for the Products table

class Product(models.Model): # This is 'Product'table in the database 
    name = models.CharField(max_length = 100)
    price= models.PositiveIntegerField()
    pic = models.ImageField(upload_to ="products/", null = True)