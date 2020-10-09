from django.db import models
from django.contrib.auth.models import User
import datetime
import django.utils

# MODELS:

# CITY MODEL
class City(models.Model):
    name = models.CharField(max_length=50)
    photo = models.CharField(max_length=500)
    # TODO photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name



# USER MODEL
class Profile(models.Model):
    name = models.CharField(max_length=50, default='default_name')
    image = models.CharField(max_length=500, default="https://moonvillageassociation.org/wp-content/uploads/2018/06/default-profile-picture1.jpg")
    join_date = models.DateField(default=django.utils.timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    current_city = models.CharField(max_length=50, default="Hometown, USA")
    # TODO look into later how to not delete associated profiles

    def __str__(self):
        return self.user.username



# POST MODEL
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2500)
    posted_date = models.DateField(default=django.utils.timezone.now)
    image = models.CharField(max_length=500)

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# COMMENT MODEL
# TODO Create comment model

