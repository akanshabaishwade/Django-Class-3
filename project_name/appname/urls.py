from django.urls import path
from .views import * # . = root path

from appname import views 
from .api import *



# {{base url}}/app(prefix)/home/

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'), 
    path('student-curd/', views.get_students, name='student_list'),  # URL for student list
    path('students/', views.student_list, name='student_list'),  # URL for student list
    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    

    # api
    path('all-student/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),

    
  
]