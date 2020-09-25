from django.db import models

# Create your models here.
class engineerregister(models.Model):
    FirstName=models.CharField(max_length=50)
    Qualification=models.CharField(max_length=50)
    workexpierience=models.IntegerField()
    emailid=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    LastName=models.EmailField()
    selectgender=models.CharField(max_length=50)
    dateofbirth=models.DateField()



class farmerregistration(models.Model):
    Name1=models.CharField(max_length=50)
    Name2=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    date=models.DateField()
    options=models.CharField(max_length=50)
    idnumber=models.TextField()
    address=models.TextField()
    pincode=models.IntegerField()
    mailid = models.EmailField()
    phonenumber=models.IntegerField()


class cropregistration(models.Model):
    user=models.CharField(max_length=40,default="local")
    ids=models.TextField()
    name=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    soil=models.CharField(max_length=50)
    start=models.DateField()
    end=models.DateField()
    irrigation=models.CharField(max_length=50)
    farming=models.CharField(max_length=50)

class farmerquiries(models.Model):
    fid=models.EmailField()
    quiry=models.CharField(max_length=50)
    fileup=models.FileField(upload_to='images/')
    status=models.CharField(max_length=50)


class contact(models.Model):
    firstname=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    mail=models.EmailField()
    qstn=models.CharField(max_length=50)

class typesofcrops(models.Model):
    name=models.CharField(max_length=50,default='')
    time=models.IntegerField(default='')
    soil=models.CharField(max_length=50,default='')
    season=models.CharField(max_length=50,default='')
    description=models.TextField(default='')

