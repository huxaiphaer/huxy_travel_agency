from rest_framework import generics

from .models import TourPackages, Destinations
from .serializer import TourPackagesSerializer, DestinationSerializer


class TourList(generics.ListCreateAPIView):
    queryset = TourPackages.objects.all()
    serializer_class = TourPackagesSerializer


class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourPackages.objects.all()
    serializer_class = TourPackagesSerializer


class DestinationList(generics.ListCreateAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestinationSerializer


class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestinationSerializer
