from django.urls import path
from subscription.views import SubscriptionView

urlpatterns = [
    path("subscription/", SubscriptionView.as_view(), name="subscription"),
    ]
