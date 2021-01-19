from django.urls import path
from News_app import views

urlpatterns = [
      path('news/', views.news, name='news'),
    path('detail/<int:pk>/', views.news_details, name='news_details'),
    path('create/', views.news_create, name='news_create'),
     path('news/draft/', views.news_draft, name='news_draft'),
     path('publish/<int:pk>/', views.news_publish, name='news_publish'),
     path('edit/<int:pk>/', views.news_edit, name='news_edit'),
     path('delete/<int:pk>/', views.news_delete, name='news_delete'),
]
