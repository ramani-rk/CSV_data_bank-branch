from django.db import models

# Create your models here.


class Bank(models.Model):
    bname=models.CharField(max_length=100)

    def __str__ (self):
        return self.bname

class Branch(models.Model):
    bname=models.ForeignKey(Bank,on_delete=models.CASCADE)
    ifsc=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    address=models.TextField()
    contact=models.IntegerField()
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)

    def __str__ (self):
        return self.branch