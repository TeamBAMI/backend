import json
import logging
import random

from users.models import User
from rest_framework import viewsets, permissions, status, renderers
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@action(
    detail=False, methods=["get"]
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    @action(
        detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated]
    )
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(
        detail=False, methods=["get"]
    )
    def obtain_approved_businesses(self, request):
        # data = User.objects.all().values()
        data = User.objects.filter(type=User.Types.APPROVED_BUSINESS).values()
        return Response({"data": data})

    @action(
        detail=False, methods=["get"]
    )
    def obtain_random_business(self, request):
        random_business = random.choice(User.objects.all().values_list())
        return Response({'data': random_business})