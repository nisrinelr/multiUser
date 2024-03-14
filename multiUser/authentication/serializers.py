from rest_framework_simplejwt.tokens import Token
from authentication.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password', 'phone_number', 'user_type')
        extra_kwrgs = {'password':{'write_only':True}}
        
    def validate(self, data):
        email = data.get('email')
        phone_number = data.get('phone_number')
        if not email and not phone_number:
            raise serializers.ValidationError("Email or Phone number is required.")
        
        data['username'] = email or phone_number
        return data
    
    
class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['user_type'] = user.user_type
        
        return token
    
