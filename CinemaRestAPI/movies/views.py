from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


# EndPoints
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='Action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='Comedy')
    serializer_class = MovieSerializer


class CriminalViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='Criminal')
    serializer_class = MovieSerializer