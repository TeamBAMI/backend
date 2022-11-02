from .models import User
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


def is_valid_type(dto):
    account_type = dto.get("type")

    if account_type == User.Types.APPROVED_BUSINESS:
        raise serializers.ValidationError(
            "Cannot create an account with type APPROVED_BUSINESS"
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "type", "password"]
        validators = [
            is_valid_type,
        ]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(UserSerializer, self).create(validated_data)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
