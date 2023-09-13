from django.db import models
from django.urls import reverse

# Create your models here.

class Person(models.Model):
    SHIRT_SIZES = [
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large')
    ]
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    class Meta:
        db_table = "Person"

    def get_absolute_url(self):
        return reverse('class_app:details', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name 
    
    