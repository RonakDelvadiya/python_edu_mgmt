from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils import timezone

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
       Token.objects.create(user=instance)

# model University
class University(models.Model):
    name = models.CharField(verbose_name="University",max_length = 100)
    website = models.CharField("Website",max_length=50,null=True,blank=True)
    is_active = models.BooleanField("Is active",default=True)
    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return self.name

#model School
class School(models.Model):
    creator = models.ForeignKey(User)
    owner = models.ForeignKey(User,related_name='Owners',blank=True,null=True)
    university = models.ForeignKey(University)
    name = models.CharField(verbose_name="School Name",max_length = 50)
    logo = models.ImageField(verbose_name="Logo",max_length = 255,upload_to="media/")
    website = models.CharField("Website",max_length=50,null=True,blank=True)
    is_active = models.BooleanField("Is active",default=True)
    created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return self.name

#model Address
class Address(models.Model):
    COUNTRY = (
        ('india',  'India'),
        ('uk',  'UK'),
        ('usa',  'USA'),
        ('china',  'China'),
        ('nepal',  'Nepal'),
    )
    street_1 = models.CharField(verbose_name="Street 1",max_length=50)
    street_2 = models.CharField(verbose_name="Street 2",max_length=50)
    city = models.CharField(verbose_name="City",max_length=50)
    state = models.CharField(verbose_name="State",max_length=50)
    country = models.CharField(verbose_name="Country",max_length=50,choices=COUNTRY)
    zipcode = models.IntegerField(verbose_name="Zipcode",max_length=6,null=True,blank=True)
    mobile = models.IntegerField(verbose_name="Mobile",unique=True,max_length=13,null=True,blank=True)

    def __str__(self):
        return "--->  "+self.street_1 +" , "+ self.street_2 +" , "+ self.city + " , "+self.state


#model Student
class Student(models.Model):
    SMARTnumber = models.CharField("Smart Num.",max_length=50,unique=True,blank=True,null=True)
    school = models.ForeignKey(School)
    first_name = models.CharField("First Name",max_length=50)
    last_name = models.CharField("Last Name",max_length=50)
    email = models.EmailField("EmailID",unique=True)
    address =  models.ManyToManyField(Address,blank=True,null=True)
    roll_no = models.PositiveIntegerField("Roll No.",unique=True)
    date_of_birth = models.DateField("Birthdate")
    is_active = models.BooleanField("Is active",default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_address(self):
        return "\n".join([p.address for p in self.address.all()])

    def __str__(self):
		return self.address
