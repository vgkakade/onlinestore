from django.db import models
from django.core import validators
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
]

ADDRESS_TYPE =[
    ('Home', 'Home 7am - 9pm'),
    ('Office', 'Office 10am - 6pm')
]


class UserRegister(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    userId = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    mobile = models.IntegerField(validators=[validators.MaxLengthValidator(10)])
    pincode = models.IntegerField()
    city = models.CharField(max_length=25)
    streetname = models.CharField(max_length=150)
    landmark = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=30)
    type = models.CharField(choices=ADDRESS_TYPE, max_length=25, blank=True)

    class Meta:
        db_table = "tblUserAddress"

    def __str__(self):
        return self.fullname
