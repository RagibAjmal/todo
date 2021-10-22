from django.db.models import fields
from .models import TodoListItem
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListItem
        fields = ("content","id")