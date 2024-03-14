from django.shortcuts import render
from rest_framework import generics, status
from subscription.models import Subscription, SubscriptionPlan
from subscription.serializers import SubscriptionSerializer, SubscriptionPlanSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsPlanSubscriber
# Create your views here.

class SubscriptionView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = IsAuthenticated, IsPlanSubscriber
    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
    