from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', views.student_detail, name='detail'),
    path('update/<int:pk>', views.StudentUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.StudentDelete.as_view(), name='delete'),
]
