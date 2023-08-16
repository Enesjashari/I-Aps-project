from rest_framework import serializers
from .models import Author, Category, Paper

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = ['id', 'name']
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['id', 'name']
        fields = '__all__'

class PaperSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Paper
        # fields = ['id', 'title', 'abstract', 'authors', 'categories', 'publication_date']
        fields = '__all__'
