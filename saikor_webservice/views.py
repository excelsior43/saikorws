from saikor_webservice.models import Saikorian
from saikor_webservice.serializers import SaikorianSerializer
from rest_framework import generics


class SaikorianList(generics.ListCreateAPIView):
    queryset = Saikorian.objects.all()
    serializer_class = SaikorianSerializer


class SaikorianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saikorian.objects.all()
    serializer_class = SaikorianSerializer