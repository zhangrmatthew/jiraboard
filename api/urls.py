from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('boards/', views.BoardViewSet.as_view()),
    path('boards/<str:pk>', views.SingleBoardViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)