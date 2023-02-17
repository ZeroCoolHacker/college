from django.shortcuts import render
from teachers.models import Teacher
# Create your views here.

def teachers_list(request):
    teachers = Teacher.objects.all()
    context = {
        "teachers" : teachers
    }
    return render(request, "teachers_list.html", context= context)
    