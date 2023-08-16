from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author, Category, Paper
from .serializers import AuthorSerializer, CategorySerializer, PaperSerializer

class PaperList(APIView):
    def get(self, request):
        papers = Paper.objects.all()
        serializer = PaperSerializer(papers, many=True)
        return Response(serializer.data)

class PaperDetail(APIView):
    def get(self, request, pk):
        paper = Paper.objects.get(pk=pk)
        serializer = PaperSerializer(paper)
        return Response(serializer.data)


class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

class AuthorDetail(APIView):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

# Similarly, create views for AuthorList, AuthorDetail, CategoryList, and CategoryDetail
