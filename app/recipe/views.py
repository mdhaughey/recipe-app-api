"""
Views for the recipe API
"""
from django.shortcuts import render

from rest_framework import viewsets #type: ignore
from rest_framework.authentication import TokenAuthentication #type: ignore
from rest_framework.permissions import IsAuthenticated #type: ignore

from core.models import Recipe
from recipe import serializers

# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')