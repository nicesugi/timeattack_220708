from rest_framework import serializers
from post.serializers import JobPostSerializer
from .models import (
    User,
    UserApplication
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_type", "password", "email", "fullname", "username"]
        
        
class UserApplicationSerializer(serializers.ModelSerializer):
    username = UserSerializer(many=True, read_only=True, source="user_set")
    company = JobPostSerializer(many=True, read_only=True, source="jobpost_set")
    

    
    class Meta:
        model = UserApplication
        fields = "__all__"