from django.urls import path
from subscription.views import SubscriptionView, CreatePlan

urlpatterns = [
    path("subscription/", SubscriptionView.as_view(), name="subscription"),
    path("create-plan/", CreatePlan.as_view(), name="create-plan")
    ]
