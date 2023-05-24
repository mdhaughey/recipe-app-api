"""Views forthe user API"""
from rest_framework import generics  # type: ignore
from rest_framework.authtoken.views import ObtainAuthToken  # type: ignore
from rest_framework.settings import api_settings  # type: ignore
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = AuthTokenSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES
