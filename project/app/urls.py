from django.urls import path
from .views import PaperList, PaperDetail, AuthorList, AuthorDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('papers/', PaperList.as_view(), name='paper-list'),
    path('papers/<int:pk>/', PaperDetail.as_view(), name='paper-detail'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]
