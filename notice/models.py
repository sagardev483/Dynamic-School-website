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
    motto = models.CharField(max_length=300, blank=True, null=True)

    description = models.TextField(
        default="A School Focused on Quality", blank=True, null=True
    )

    heading_activities = models.CharField(max_length=100, blank=True)
    extra_activities = models.TextField(
        default="Our Activities", blank=True, null=True
    )  # Ensure default value

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery_images/")

    def __str__(self):
        return self.image.url
