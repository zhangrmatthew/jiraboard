from rest_framework import serializers
from .models import Board, User, Task, Column

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'boards')

class BoardSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)
    class Meta:
        model = Board
        fields = ('id', 'username', 'password','users')