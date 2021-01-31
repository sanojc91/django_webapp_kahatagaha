from django.db import models
from django.utils import timezone

# Create your models here.


class Slider(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50, blank=True)
    text = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to='images/')
    position = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.position


class Posts(models.Model):
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/', blank=True)
    image_3 = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200, default= 'Khatagaha Graphite Lanaka Limited updates')
    content = models.TextField()
    author = models.CharField(max_length=50)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Product(models.Model):
    product_image = models.ImageField(upload_to='images/')
    product_name = models.CharField(max_length=70)
    carbon_grade_1 = models.CharField(max_length=10)
    grade_1_availability = models.CharField(max_length=15, default='Available')
    carbon_grade_2 = models.CharField(max_length=10, blank=True)
    grade_2_availability = models.CharField(max_length=15, blank=True)
    carbon_grade_3 = models.CharField(max_length=10, blank=True)
    grade_3_availability = models.CharField(max_length=15, blank=True)
    carbon_grade_4 = models.CharField(max_length=10, blank=True)
    grade_4_availability = models.CharField(max_length=15, blank=True)
    particle_size = models.CharField(max_length=10, blank=True)
    product_summary = models.CharField(max_length=200, default='Product of Kahatagha Graphite Lanka Limited')

    def __str__(self):
        return self.product_name
