from rest_framework import serializers
from .models import Board, User, Task, Column


class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'boards')

class BoardSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    columns = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Board
        fields = ('id', 'username', 'password', 'users', 'columns')


class ColumnSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Column
        fields = ('id','name','board','tasks')

class TaskSerializer(serializers.ModelSerializer):
    column = serializers.PrimaryKeyRelatedField(queryset=Column.objects.all())
    assignment = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Task
        fields = ('id','name','assignment','created','assignment_date','description','acceptance_criteria','column')
