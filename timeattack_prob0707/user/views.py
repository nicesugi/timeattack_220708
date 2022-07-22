import json
import datetime
from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from user.permissions import IsCandidateUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import login, authenticate, logout

from user.serializers import UserApplicationSerializer
from .models import User, UserApplication, UserLog, UserType


class SignUpView(APIView):

    permission_classes = [permissions.AllowAny]
    # 회원 가입
    def post(self, request):
        # data = json.loads(request.body)
        user_type = request.data.get('user_type', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        # User.objects.create(email=email, password=password)
        usertype = UserType.objects.get(user_type = user_type)

        # passcode = make_password(password)
        # print("usertype=", end=""), print(usertype)
        # User(email=email, password=make_password(password)).save()
        User(user_type=usertype, email=email, password=make_password(password)).save()

        return Response(status=status.HTTP_200_OK)


class SignInView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(request, email=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        now = datetime.datetime.now()
        UserLog.objects.create(user=user, last_login_date=now.strftime('%Y-%m-%d')) # 유저 로그 생성
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!!"}, status=status.HTTP_200_OK)


class UserApplicationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCandidateUser]
    
    def get(self, request):
        applications = UserApplication.objects.filter(user=request.user)
        serialized_data = UserApplicationSerializer(applications, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def post(self, request):

        request.data["user"] = request.user.id
        application_serializer = UserApplicationSerializer(data=request.data)

        if application_serializer.is_valid():
            application_serializer.save()
            return Response(application_serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(application_serializer.errors, status=status.HTTP_400_BAD_REQUEST)