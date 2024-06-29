from rest_framework.routers import DefaultRouter
from django.urls import path, include

from profiles.views import PatientProfileView


router = DefaultRouter()
router.register("patient-profile", PatientProfileView, basename="patient-profile")


urlpatterns = [
    path("", include(router.urls)),
]
