from django.contrib.auth import authenticate,login
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializer import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt   
def Login(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        email = data.get('email')
        password = data.get('pass')
        print(f'Email: {email}, Password: {password}')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            print("Login successful")
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    
@csrf_exempt
def add_user(request):
    if request.method =='POST':
        data=json.loads(request.body)
        name=data.get('name')
        email = data.get('email')
        password=data.get('pass')
        address=data.get('address')
        phone=data .get('phone')
        user=data.get('user')
        print(f'Name: {name}, Email: {email}, Password: {password}, Address: {address}, Phone: {phone}, User: {user}')


@api_view(['GET'])
def cropsdetail(request):
    crops=crops_detail.objects.all()
    serializer=CropdetailSerializer(crops,many=True)
    return Response(serializer.data)