from .views import ListVideo, DetailVideo
from django.urls import path, re_path

urlpatterns = [
    path("", ListVideo.as_view(), name="list_video"),
    re_path("(?P<id>[0-9])", DetailVideo.as_view(), name="detail_video"),
]