from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from cookie_storage.helpers import SessionHelper
from demo.api.serializers import UserSerializer
from demo.models import User


class UserDemoAPIView(APIView):
    """Set/Get user data in Session
    no auth required
    """
    serializer_class = UserSerializer
    model_class = User
    permission_classes = (AllowAny,)

    def get(self, request):
        session = SessionHelper(request)
        instance = session.get(self.model_class)
        serializer = self.serializer_class(instance=instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data
        serializer = self.serializer_class(data=payload)
        serializer.is_valid(raise_exception=True)
        instance = self.model_class(**serializer.validated_data)
        session = SessionHelper(request)
        session.set(instance)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
