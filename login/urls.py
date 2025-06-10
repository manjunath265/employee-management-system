from django.urls import path
from login.views import CustomAuthToken

urlpatterns = [
    path('api/login/', CustomAuthToken.as_view()),
]