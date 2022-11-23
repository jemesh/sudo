from django.db import models
from django.core.validators import RegexValidator
# usermodel
class usermodel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mob=RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+99-0123456789'.")
    mobile=models.CharField(validators=[mob],max_length=13,unique=True)
    def __str__(self):
        return self.first_name
#customer model ,which is related to usermodel with one to one relationship
class customer(models.Model):
    pmk=models.OneToOneField(usermodel,on_delete=models.CASCADE,primary_key=True)
    profile_no=models.IntegerField()
