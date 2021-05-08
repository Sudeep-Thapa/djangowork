from django.db import models

# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    subject=models.TextField(blank="True")
    message=models.TextField()

    def __str__(self):
        return self.name
class Review(models.Model):
    name = models.CharField(max_length=300)
    post=models.CharField(max_length=300)
    image=models.TextField()
    review=models.TextField()

    def __str__(self):
        return self.name
class Information(models.Model):
    address=models.TextField()
    street=models.TextField()
    phone=models.IntegerField()
    time=models.TextField()
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.address
