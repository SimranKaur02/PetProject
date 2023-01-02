from django.urls import path
from .views import *

urlpatterns = [
     path('dept/',DepartmentList.as_view()),
     path('dept/<int:pk>/', DepartmentDetail.as_view()),
     path('student/', StudentList.as_view()),
     path('student/<int:pk>/', StudentDetail.as_view()),
     path('form/',index),
     path('celery/', test, name='test'),
     path('sendmail/', send_mail_to_all, name='sendmail')
]