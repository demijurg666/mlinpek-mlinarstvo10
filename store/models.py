from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)

    modified = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    instock = models.IntegerField(default=0, null=True, blank=True)

    modified = models.CharField(max_length=200, null=True)

    def get_absolute_url(self):
        return reverse("trgovina", kwargs={})
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Izdavastvo(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    instock = models.IntegerField(default=0, null=True, blank=True)
    description = models.CharField(max_length=900, null=True, blank=True)
    izdavac = models.CharField(max_length=200, null=True, blank=True)
    godinaIzdanja = models.CharField(max_length=200, null=True, blank=True)

    modified = models.CharField(max_length=200, null=True)

    
    def get_absolute_url(self):
        return reverse("izdavastvo", kwargs={})

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




class Kurs(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    modified = models.CharField(max_length=200, null=True)

    def get_absolute_url(self):
        return reverse("kurs", kwargs={})

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    modified = models.CharField(max_length=200, null=True)

        
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all() #ovde je vrv problem u ovom set all
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_cart_list(self):
        orderitems = self.orderitem_set.all() 
        result = {}
        for item in orderitems:
            #print(item.product, item.quantity)
            result[item.product]=item.quantity
        #print(result)
        return result        


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    
    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse("cart", kwargs={})
        

 #kako klasa order koristi get_total funkciju iz OrderItem kada je pre napisana???   

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added =  models.DateTimeField(auto_now_add=True)

    modified = models.CharField(max_length=200, null=True)


    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
        
    def __str__(self):
        return str(self.product)
    

from embed_video.fields import EmbedVideoField    


class Video(models.Model):
    title = models.CharField(max_length=100)
    url = EmbedVideoField()
    
    def __str__(self):
        return str(self.title)