from django.db import models

# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(default="no description", blank=True)
    image = models.ImageField(upload_to="notice/images/", blank=True, null=True)

    def __str__(self):
        return self.title
