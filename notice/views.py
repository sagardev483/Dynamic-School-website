from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Notice, Nav, School, Teacher, Gallery
from django.views.generic import TemplateView

# Create your views here.


def notice_api(request):
    notices = list(Notice.objects.all().values("title", "date", "description", "image"))

    for notice in notices:
        if notice["image"]:  # Ensure full media URL
            notice["image"] = request.build_absolute_uri(
                settings.MEDIA_URL + notice["image"]
            )

    return JsonResponse({"notices": notices})


class HomeView(TemplateView):
    template_name = "notice/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["navbar"] = Nav.objects.all()
        context["school"] = School.objects.first()
        context["teacher"] = Teacher.objects.all()
        context["gallery"] = Gallery.objects.all()
        return context
