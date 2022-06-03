from rest_framework import serializers
from .models import Board, User, Task, Column


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'boards')

class BoardSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = ('id', 'username', 'password', 'users')



