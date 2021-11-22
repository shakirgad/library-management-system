from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)
    def __str__(self):
        return self.name
  
class Book(models.Model):
    status_book=[
        ('aval','aval'),
        ('rent','rent'),
        ('sol','sol'),
    ] 
    
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photos' , null=True,blank=True)
    photo_author = models.ImageField(upload_to='photo' ,null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=4 , decimal_places=2,null=True,blank=True)
    rate_price_day =  models.DecimalField(max_digits=4 , decimal_places=2,null=True,blank=True)
    rental_period = models.IntegerField(null=True , blank=True)
    total_rental = models.DecimalField(max_digits=4 , decimal_places=2,null=True,blank=True)
    active =  models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices=status_book,null=True,blank=True)
    Category = models.ForeignKey('Category', on_delete = models.PROTECT)
    
    

    def __str__(self):
        return self.title 

    
 


