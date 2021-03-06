from rest_framework import serializers
from .models import Recipe, Category


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id',
                  'title',
                  'summary',
                  'description',
                  'slug',
                  'prep_time',
                  'ctime',
                  'mtime',
                  'sources',
                  'category',
                  'serving_value',
                  'get_directions',
                  )