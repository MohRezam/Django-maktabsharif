from django.db import models
from django import forms

# Create your models here.
SKILL_CHOICES = (("PYTHON", "python"), ("HTML", "html"), ("CSS", "css"), ("JAVA SCRIPTS", "Java Scripts"), ("C", "C"), ("C++", "C++"), ("PHP", "PHP"))


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    skill = models.CharField(max_length=20, choices=SKILL_CHOICES, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}'s user profile"
    
    
