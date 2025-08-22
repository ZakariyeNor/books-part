from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path('book/<int:pk>/', views.BookDetailAPIView.as_view(), name='book-detail'),
]