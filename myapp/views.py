from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from myapp.models import *
from myapp.serializer import *

class Studentvset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentser
