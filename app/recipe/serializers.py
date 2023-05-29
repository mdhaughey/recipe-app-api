"""Serializers for the recipe API view"""

from rest_framework import serializers #type: ignore

from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link',]
        read_only_fields = ['id']

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for REcipe detail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']