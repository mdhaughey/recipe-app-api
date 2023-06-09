"""
Views for the recipe API
"""
from rest_framework import (  # type: ignore
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication  # type: ignore
from rest_framework.permissions import IsAuthenticated  # type: ignore

from core.models import (
    Recipe,
    Tag,
)
from recipe import serializers

# Create your views here.


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for user"""
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Return the serializer class"""
        if self.action == "list":
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TagViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """Manage Tags in the DB"""

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for user"""
        return self.queryset.filter(user=self.request.user).order_by("-name")
