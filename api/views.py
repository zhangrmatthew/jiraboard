from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BoardSerializer, UserSerializer
from .models import Board, User

class BoardViewSet(APIView):
    """
    List all boards
    """
    def get(self, request, format=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

class BoardCreate(APIView):
    '''
    Create a board
    '''
    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            #get resulting user model, then update board?
            boards = serializer.save()
            user = User.objects.filter(id=request.data["users"][0])
            if(user):
                boards.users.add(request.data["users"][0])
                boards.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleBoardViewSet(APIView):
    """
    Get specific board
    """
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)


    #TODO add update and delete cols/tasks

class UserViewSet(APIView):
    """
    List all users or create new user
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleUserViewSet(APIView):
    """
    Get specific user
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = UserSerializer(users)
        return Response(serializer.data)

    #add board to user here 

    #TODO add linkage to boards and tasks when created some

 