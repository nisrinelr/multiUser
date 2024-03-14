from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from subscription.models import Subscription, SubscriptionPlan

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ('name', 'price', 'description')
    def validate(self, attrs):
        user = self.context['request'].user
        if user.is_anonymous:
            raise AuthenticationFailed("Authentication credentials were not provided")
        return super().validate(attrs)
    
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('plan', 'status', 'expiration_date')
    def validate(self, attrs):
        user = self.context['request'].user
        if user.is_anonymous:
            raise AuthenticationFailed("Authentication credentials were not provided")
        if Subscription.objects.filter(user=user ,status=True).exists():
            raise ValidationError("You are already subscribed to another plan.")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user_id'] = user.id
        return super().create(validated_data)