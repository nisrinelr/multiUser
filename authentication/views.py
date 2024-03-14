from django.shortcuts import render
from rest_framework.request import Request
from authentication.serializers import SignUpSerializer, LoginSerializer
from rest_framework import generics, status
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access' : str(refresh.access_token),
        }
        
        return Response(data, status=status.HTTP_200_OK)
    
    
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    def post(self, request: Request, *args, **kwargs):
        
        response = super().post(request, *args, **kwargs)
        return response
    
