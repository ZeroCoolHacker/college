from django.shortcuts import render, redirect
from students.models import Student
from College import urls
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

def add_student(request):
    if request.method == "GET":
        return render(request, "add_student.html")
    elif request.method == "POST":
        add_student = Student()
        add_student.first_name = request.POST["first_name"]
        add_student.last_name = request.POST["last_name"]
        add_student.date_of_birth = request.POST["dob"]
        add_student.fee = request.POST["fee"]
        add_student.student_class = request.POST["course"]
        add_student.roll_number = request.POST["roll_number"]
        
        add_student.save() # this query save the object data in database
        return redirect('college/student/list')
    
