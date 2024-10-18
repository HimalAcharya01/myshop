from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
class Subcategory(models.Model):
    title=models.CharField(max_length=200)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
class Brand(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
Availability_fields=(
    ('pre_order','pre_order'),
    ('In stock','In stock'),
    ('Out of Stock','out of stock')
)


class Product(models.Model):
    image=models.ImageField(upload_to='products',null=True,blank=True)
    image2=models.ImageField(upload_to='products',null=True,blank=True)
    image3=models.ImageField(upload_to='products',null=True,blank=True)
    name=models.CharField(max_length=30)
    Brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    desc=RichTextField(blank=True)
    Availability=models.CharField(max_length=200,choices=Availability_fields,null=True)
    mark_price=models.DecimalField(max_digits=10,decimal_places=2)
    dicscount_percentage=models.DecimalField(max_digits=10,decimal_places=2)
    price=models.DecimalField(max_digits=10,decimal_places=2,editable=False)

    def save(self,*args,**kwargs):
        self.price=self.mark_price*(1-self.dicscount_percentage/100)
        super().save(*args,*kwargs)

    def __str__(self) -> str:
        return self.name
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='images',null=True,blank=True)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.user.username

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField()
    coment=models.TextField()
    date=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.product.name

class Order(models.Model):
    product=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField()
    total=models.CharField(max_length=300)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    ispay=models.BooleanField(default=False)
    date=models.DateTimeField(default=datetime.now())
    image=models.ImageField(upload_to='order/image')


    def __str__(self) -> str:
        return self.product
    