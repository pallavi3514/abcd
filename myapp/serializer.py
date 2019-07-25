from rest_framework.serializers import ModelSerializer
from myapp.models import *
class Studentser(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
