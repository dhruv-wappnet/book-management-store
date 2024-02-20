from django.db import models
# import user model
from django.contrib.auth.models import User, Group
from datetime import timedelta, datetime

class BookStoreUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.username

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    valid_till = models.DateTimeField(default=datetime.now() + timedelta(days=7))

    def __str__(self):
        return f"{self.user.username} ordered {self.quantity} of {self.book.title} on {self.order_date}."