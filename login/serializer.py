from rest_framework import serializers
from .models import Login

# User Serializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields= '__all__'
        