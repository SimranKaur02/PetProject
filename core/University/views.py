from django.http import HttpResponse
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from .forms import *
from .templates import *
from .tasks import test_func
from send_mail_app.tasks import send_mail_func

# Create your views here.

class DepartmentList(generics.ListCreateAPIView):
     serializer_class = DepartmentSerializer
     queryset = Department.objects.all()


#PUT/DELETE
class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = DepartmentSerializer
     queryset = Department.objects.all()


class StudentList(generics.ListCreateAPIView):
     serializer_class = StudentSerializer
     def get_queryset(self):
          queryset = Student.objects.all()
          department = self.request.query_params.get('department')
          if department is not None:
               queryset = queryset.filter(dept=department)
          return queryset


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = StudentSerializer
     queryset = Student.objects.all()


def index(request):
     form = StudentForm()

     if request.method == 'POST':
          print('hello',request.POST)
          form = StudentForm(request.POST)
          if form.is_valid():
               form.save()

     context = {'form': form}
     return render(request, 'index.html', context)


#celery
def test(request):
     test_func.delay()
     return HttpResponse('Done')

def send_mail_to_all(request):
     send_mail_func.delay()
     return HttpResponse('Sent')




