from django.urls import path
from authentication.views import SignUpView, LoginView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name='user-signup'),
    path("login/", LoginView.as_view(), name='user-login'),
]
