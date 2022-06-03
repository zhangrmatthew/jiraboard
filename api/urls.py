from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('boards/create', views.BoardCreate.as_view()),
    path('boards/get/<str:pk>', views.SingleBoardViewSet.as_view()),
    path('boards/', views.BoardViewSet.as_view()),
    path('users/', views.UserViewSet.as_view()),
    path('users/<str:pk>', views.SingleUserViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)