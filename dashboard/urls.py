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

    path(
        "air-minum/",
        views.air_minum,
        name="air_minum"
    ),

    path(
        "download/air-minum/",
        views.download_air,
        name="download_air"
    ),

    path(
        "kepemilikan-lahan/",
        views.lahan,
        name="lahan"
    ),

    path(
        "download/lahan/",
        views.download_lahan,
        name="download_lahan"
    ),

    path(
        "status-kesejahteraan/",
        views.kesejahteraan,
        name="kesejahteraan"
    ),

    path(
        "download/kesejahteraan/",
        views.download_kesejahteraan,
        name="download_kesejahteraan"
    ),

    path(
        "kepemilikan-rumah/",
        views.rumah,
        name="rumah"
    ),

    path(
        "download/rumah/",
        views.download_rumah,
        name="download_rumah"
    ),
]