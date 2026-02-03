from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>/', views.student_detail, name='detail'),
    path('update/<int:pk>/', views.StudentUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.StudentDelete.as_view(), name='delete'),
	path('api/students/', views.StudentsAPIView.as_view(), name='api'),
	path('api/students/<int:pk>/', views.StudentDetailAPIView.as_view()),
	path('api/students/create/', views.StudentCreateAPIView.as_view()),
	path('api/students/<int:pk>/update/', views.StudentUpdateAPIView.as_view()),
	path('api/students/<int:pk>/delete/', views.StudentDeleteAPIView.as_view()),
]
