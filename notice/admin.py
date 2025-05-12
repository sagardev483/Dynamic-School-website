from django.contrib import admin
from django import forms
from .models import Notice
import nepali_datetime

# Register your models here.

admin.site.register(Notice)


class NoticeForm(forms.ModelForm):
    date_bs = forms.CharField(label="Date (B.S.)", required=False)
