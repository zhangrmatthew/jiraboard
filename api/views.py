from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BoardSerializer
from .models import Board

class BoardViewSet(APIView):
    """
    List all boards, or create a new board.
    """
    def get(self, request, format=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
