from django.db import models

# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(default="no description", blank=True)
    image = models.ImageField(upload_to="notice/images/", blank=True, null=True)

    def __str__(self):
        return self.title


class Nav(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=250)
    motto = models.CharField(max_length=300)
    description = models.TextField()
    extra_activities = models.TextField()

    def __str__(self):
        return self.name
