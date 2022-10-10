from .models import User
from django.contrib.auth.models import Group
from rest_framework import serializers


def is_valid_type(type):
    if not type in [User.Types.BUSINESS, User.Types.STUDENT]:
        raise serializers.ValidationError("Invalid type")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "type"]
        validators = [
            is_valid_type,
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
