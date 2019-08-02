from django.urls import path
from RESTAPI import views
urlpatterns = [
    path('', views.home),
    path('user', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('question/', views.QuestionList.as_view()),
    path('question/<int:pk>', views.QuestionDetail.as_view()),
    path('answer', views.AnswerList.as_view()),
    path('answer/<int:pk>', views.AnswerDetail.as_view()),
    path('search/advanced', views.Search.as_view()),
]
