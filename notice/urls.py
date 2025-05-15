from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomeView, notice_api


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("api/notices/", notice_api, name="notice-api"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
