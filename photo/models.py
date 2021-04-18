from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


class Photos(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.ImageField(null=True, blank=True, upload_to='media')
    using_count = models.IntegerField(default=0)
    gender = models.CharField(max_length=20)
    quality = models.CharField(max_length=10)
    type = models.IntegerField(default=0)
    
    answer1 = models.IntegerField(default=0)
    answer2 = models.IntegerField(default=0)
    answer3 = models.IntegerField(default=0)

class Counter(models.Model):
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField(default=0)
    ids = ArrayField(models.IntegerField(), size=24,)
    ans1 = ArrayField(models.IntegerField(), size=24,)
    ans2 = ArrayField(models.IntegerField(), size=24,)
    ans3 = ArrayField(models.IntegerField(), size=24,)