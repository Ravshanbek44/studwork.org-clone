from django.urls import path
from . import views

urlpatterns = [
    path('list-worktype/', views.WorkTypeListAPIView.as_view()),
    path('work-create/', views.WorkCreateAPIView.as_view()),
    path('work-detail/<int:pk>/', views.WorkDetailAPIView.as_view()),
    path('work-update/<int:pk>/', views.WorkUpdateAPIView.as_view()),
    path('work-delete/<int:pk>/', views.WorkDeleteAPIView.as_view()),
    path('work-list/', views.WorkListAPIView.as_view()),

    path('comment-list/', views.CommentListAPIView.as_view()),
    path('comment-create/', views.CommentCreateAPIView.as_view()),
    path('otclick/', views.ClickCreateAPIView.as_view()),
    path('list-otclick/', views.OtClickListAPIView.as_view()),
    path('my-works/', views.MyWorksListAPIView.as_view()),
    path('give-work/', views.GiveWorkCreateAPIView.as_view())
]
