from django.db import models

# Create your models here.
class PersonalInformation(models.Model):
    name=models.CharField(max_length=10)
    lastname=models.CharField(max_length=20)
    about=models.TextField(blank=True)
    address=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    email=models.EmailField()
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class About(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title=models.CharField(max_length=100)
    project_description=models.TextField(blank=True)
    linku=models.TextField(blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    subject=models.TextField(blank=True)
    message=models.TextField(blank=True)

    def __str__(self):
        return self.name