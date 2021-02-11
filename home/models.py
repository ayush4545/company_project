from django.db import models

# Create your models here.
# Models in Django is similar to Table in Database


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):
        return 'Message From '+self.name
    