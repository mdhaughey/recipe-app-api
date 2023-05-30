"""Serializers for the recipe API view"""

from rest_framework import serializers  # type: ignore

from core.models import (
    Recipe,
    Tag,
)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
        ]
        read_only_fields = ["id"]


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for REcipe detail view"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ["description"]


class TagSerializer(serializers.ModelSerializer):
    """Serailizer for tags"""

    class Meta:
        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id"]
