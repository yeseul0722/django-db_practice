from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.music_list_create),   # 모든 음악 정보 조회
    path('music/<int:music_pk>/', views.music_detail),
]
