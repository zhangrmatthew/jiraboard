import uuid
from django.db import models

# Create your models here.

class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    boards = models.ManyToManyField(Board, related_name='users', blank=True)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    assignment = models.OneToOneField(User, on_delete=models.SET_DEFAULT, default=None, null=True)
    created = models.DateTimeField
    assignment_date = models.DateTimeField
    description = models.TextField(blank=True,null=True)
    acceptance_criteria = models.TextField(blank=True,null=True)
    
class Column(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


