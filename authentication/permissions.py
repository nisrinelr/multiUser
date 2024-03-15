from authentication.constants import BETA_USER, COMPANY_USER, PLAN_SUBSCRIBER
from rest_framework.permissions import BasePermission
from authentication.models import User
from subscription.models import Subscription

class IsBetaUser(BasePermission):
    """
        Allow access to only authenticated users that are also Beta users
    """
    
    def has_permission(self, request, view):
        user : User = request.user
        if user is None or user.is_anonymous:
            return False
        return user.user_type == BETA_USER
    
    
class IsCompanyUser(BasePermission):
    """
        Allow access to only authenticated users that are also Company users
    """
    def has_permission(self, request, view):
        user : User = request.user
        if user is None or user.is_anonymous:
            return False
        return user.user_type == COMPANY_USER
    
class IsPlanSubscriber(BasePermission):
    """
        Allow access to only authenticated users that are also Plan subscribers
    """
    def has_permission(self, request, view):
        user : User = request.user
        if user is None or user.is_anonymous:
            return False
        return user.user_type == PLAN_SUBSCRIBER
    
class ReadOnly(BasePermission):
    """
    Allow access only for read Images ('GET', 'HEAD', 'OPTIONS')

    """
    def has_permission(self, request, view):
        return request.method in ['GET', 'HEAD', 'OPTIONS']
    
    
class IsBasicPlan(BasePermission):
    """
    Allow only subscribed Users who are also Basic plan subscribers to view this page

    """
    message = "Only Basic plan subscribers are allowed to acces this page"
    def has_permission(self, request, view):
        user : User = request.user
        if user is None or user.is_anonymous:
            return False
        return Subscription.objects.filter(user=user, plan=1)
    

class IsProPlan(BasePermission):
    """
    Allow only subscribed Users who arealso Pro plan subscribers to view this page

    """
    message = "Only Pro plan subscribers are allowed to acces this page"
    def has_permission(self, request, view):
        user : User = request.user
        if user is None or user.is_anonymous:
            return False
        return Subscription.objects.filter(user=user, plan=2)
    
class IsPremiumPlan(BasePermission):
    """
    Allow only subscribed Users who are also Premium plan subscribers to view this page

    """
    message = "Only Premium plan subscribers are allowed to acces this page"
    def has_permission(self, request, view):
        user : User = request.user
        if user is None or user.is_anonymous:
            return False
        return Subscription.objects.filter(user=user, plan=3)