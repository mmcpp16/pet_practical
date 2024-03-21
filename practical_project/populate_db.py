import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practical_project.settings')

import django
django.setup()

from pets_for_students.models import Student, Cat

def populate():
    students_data = [
        {'first_name': 'Alyssa', 'last_name': 'Croft', 'cats': ['Alex', 'Luna', 'Mittens']},
        {'first_name': 'Jone', 'last_name': 'Doe', 'cats': ['Muffins']},
        {'first_name': 'Aza,', 'last_name': 'Khan', 'cats': ['Jill', 'Joe']}, 
    ]

    for student_data in students_data:
        student, created = Student.objects.get_or_create(
            first_name=student_data['first_name'],
            last_name=student_data['last_name']
        )

        # Update number of cats for the student
        student.cat_num = len(student_data['cats'])
        student.save()

        # Add cats for the student
        for cat_name in student_data['cats']:
            cat, created = Cat.objects.get_or_create(
                name=cat_name,
                owner=student
            )

if __name__ == '__main__':
    print('Starting population script...')
    populate()
    print('Population script completed.')
