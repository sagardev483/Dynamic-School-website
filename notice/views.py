from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Notice, Nav, School


# Create your views here.


def notice_api(request):
    notices = list(Notice.objects.all().values("title", "date", "description", "image"))

    for notice in notices:
        if notice["image"]:  # Ensure full media URL
            notice["image"] = request.build_absolute_uri(
                settings.MEDIA_URL + notice["image"]
            )

    return JsonResponse({"notices": notices})


def home(request):
    navbar = Nav.objects.all()
    school = School.objects.first()
    return render(request, "notice/main.html", {"navbar": navbar, "school": school})
