import uuid
from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    assignment = models.OneToOneField(User)
    created = models.DateTimeField
    assignment__date = models.DateTimeField
    description = models.TextField(blank=True,null=True)
    acceptance__criteria = models.TextField(blank=True,null=True)
    
class Column(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    board = models.ForeignKey(Board)

class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

