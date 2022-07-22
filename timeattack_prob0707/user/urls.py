from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignInView, UserApplicationView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('sign-in', SignInView.as_view()),
        # simplejwt 에서 제공하는 기본 JWT 인증 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('application/', UserApplicationView.as_view())
]
