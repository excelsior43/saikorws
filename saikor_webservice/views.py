from saikor_webservice.models import Saikorian
from saikor_webservice.serializers import SaikorianSerializer
from rest_framework import generics


class SaikorianList(generics.ListCreateAPIView):
    queryset = Saikorian.objects.all()
    serializer_class = SaikorianSerializer
    def get_queryset(self):
        queryset = Saikorian.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        return queryset

class SaikorianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saikorian.objects.all()
    serializer_class = SaikorianSerializer
