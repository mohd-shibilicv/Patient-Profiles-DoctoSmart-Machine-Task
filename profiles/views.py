from rest_framework.viewsets import ModelViewSet

from profiles.models import PatientProfile
from profiles.serializers import PatientProfileSerializer


class PatientProfileView(ModelViewSet):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
