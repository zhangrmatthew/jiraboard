from rest_framework import serializers
from .models import Board, User, Task, Column

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'username', 'password')