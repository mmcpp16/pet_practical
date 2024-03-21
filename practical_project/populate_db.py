import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practical_project.settings')

import django
django.setup()

from pets_for_students.models import Student, Cat

def populate():
    students_data = [
        {'first_name': 'Alyssa', 'last_name': 'Croft', 'cats': ['Alex', 'Luna', 'Mittens']},
        {'first_name': 'John', 'last_name': 'Doe', 'cats': ['Muffins']},
        {'first_name': 'Azam', 'last_name': 'Khan', 'cats': ['Jill', 'Joe']}, 
    ]

    for student_data in students_data:
        student = add_student(student_data['first_name'], student_data['last_name'])
        for cat_name in student_data['cats']:
            add_cat(student, cat_name)

    for student in Student.objects.all():
        student.cat_num = student.cat_set.count()
        student.save()
        # print(f'Student: {student.full_name}, Number of cats: {student.cat_num}')
        # for cat in student.cat_set.all():
        #     print(f'- Cat: {cat.name}')

def add_student(first_name, last_name):
    student = Student.objects.get_or_create(first_name=first_name, last_name=last_name)[0]
    return student

def add_cat(student, name):
    cat = Cat.objects.get_or_create(owner=student, name=name)[0]
    return cat
if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population script completed.')
