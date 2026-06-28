from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "siswa-miskin/",
        views.siswa,
        name="siswa_miskin"
    ),

    path(
        "download/siswa/",
        views.download_siswa,
        name="download_siswa"
    ),
]