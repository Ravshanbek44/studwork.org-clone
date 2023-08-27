from django.urls import path
from . import views

urlpatterns = [
    path('project-list/', views.MarketListAPIView.as_view()),
    path('project-create/', views.MarketCreateAPIView.as_view()),
    path('project-detail/<int:pk>/', views.MarketDetailAPIView.as_view()),
    path('project-update/<int:pk>/', views.MarketUpdateAPIView.as_view()),
    path('project-delete/<int:pk>/', views.MarketDeleteAPIView.as_view()),

    path('market-full-create/', views.MarketCreateView.as_view()),
    path('file-demo-create/', views.MarketFileDemoCreateAPIView.as_view()),
    path('file-done-create/', views.MarketFileDoneCreateAPIView.as_view()),
]
