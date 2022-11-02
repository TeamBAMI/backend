from users.models import User
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import Group

from users.serializers import GroupSerializer, UserSerializer


class PostOnly(permissions.BasePermission):
    """
    Object-level permission to only allow write operations.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Only allow reads if the user is staff
            return request.user and request.user.is_staff
        else:
            return True


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [PostOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
