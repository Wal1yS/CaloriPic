from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('news/', views.news_home, name='news'),
    path('create/', views.create, name='create'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
]
