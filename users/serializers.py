from .models import User
from django.contrib.auth.models import Group
from rest_framework import serializers


def is_valid_type(dto):
    account_type = dto.get("type")

    if account_type == User.Types.APPROVED_BUSINESS:
        raise serializers.ValidationError(
            "Cannot create an account with type APPROVED_BUSINESS"
        )


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
