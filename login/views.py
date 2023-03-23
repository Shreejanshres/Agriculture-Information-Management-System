from django.contrib.auth import login
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import LoginSerializer
from .models import Login
import json
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def loginlist(request):
    login=Login.objects.all()
    serializer=LoginSerializer(login,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

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
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method'})