from django.db import models

# Create your models here.
class regist(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    phone=models.IntegerField()
    confirm=models.CharField(max_length=50)
    class Meta:
        db_table="regist"


    
class subm(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.CharField()
   
    class Meta:
        db_table="subm"

class bookng(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    service_type=models.CharField()
    preferred_time=models.DateTimeField()
    address=models.CharField()
    landmark=models.CharField(max_length=100)
    notes=models.TextField()
    class Meta:
        db_table="bookng"


class pay(models.Model):
    Card=models.CharField(max_length=100)
    number=models.IntegerField()
    EXP=models.DateField()
    cvv=models.IntegerField()
    class Meta:
        db_table="pay"
class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    message2=models.TextField()
    rating=models.IntegerField()
    class Meta:
        db_table="feedback" 