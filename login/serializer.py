from rest_framework import serializers
from .models import *

# User Serializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields= '__all__'

class CropdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = crops_detail
        fields= '__all__'
        
        