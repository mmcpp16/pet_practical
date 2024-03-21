from django.shortcuts import render
from pets_for_students.models import Student, Cat


def index(request):
    students = Student.objects.all().order_by('last_name')
    for student in students:
        student.cat_num = student.cat_set.count()
        student.save()
    context_dict = {'students': students}
    return render(request, 'pets_for_students/index.html', context_dict)

def pets(request):
    cats = Cat.objects.all().order_by('name')
    context_dict = {'cats': cats}
    return render(request, 'pets_for_students/cats.html', context_dict)