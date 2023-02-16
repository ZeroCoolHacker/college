from django.shortcuts import render
from students.models import Student
# Create your views here.
def student_lists(request):
    # students = Student.objects.all()
    students = Student.objects.filter(pass_matric=True)
    # students = Student.objects.filter(roll_number=2, first_name="Usman")
    # students = Student.objects.filter(fee=10000)
    context = {
        "students" : students
    }
    return render(request, "students_list.html", context=context)
