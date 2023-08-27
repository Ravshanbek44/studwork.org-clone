from django.urls import path
from . import views

urlpatterns = [
    path('questions-list/', views.QuestionListAPIView.as_view()),
    path('question-create/', views.QuestionCreateAPIView.as_view()),
    path('question-detail/<int:pk>/', views.QuestionDetailAPIView.as_view()),
    path('question-update/<int:pk>/', views.QuestionUpdateAPIView.as_view()),
    path('question-delet/<int:pk>/', views.QuestionDeleteAPIView.as_view()),

    path('answer-list/', views.AnswerListAPIView.as_view()),
    path('answer-create/', views.AnswerCreateAPIView.as_view()),
    path('answer-detail/<int:pk>/', views.AnswerDetailAPIView.as_view()),
    path('answer-update/<int:pk>/', views.AnswerUpdateAPIView.as_view()),
]
