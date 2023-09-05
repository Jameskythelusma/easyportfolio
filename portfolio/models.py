from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class user(models.Model):
    user_name=models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo=models.ImageField(default='profile_photo/profil.jpg', upload_to='profile_photo/')


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('design', 'Design'),
        ('programming', 'Programming'),
        ('fitness', 'Fitness'),
        ('health', 'Health'),
       ('finance','finance'),
        ('money','money'),
        ('education','education'),
        ('food','food')
                             ]
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='project_photos/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
