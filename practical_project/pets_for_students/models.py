from django.db import models

class Student(models.Model):
    FIRST_NAME_MAX_LENGTH = 50
    LAST_NAME_MAX_LENGTH = 50
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH)
    #Setting max length of names so they're not hard coded in
    cat_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cat(models.Model):
    CAT_NAME_MAX_LENGTH = 50
    name = models.CharField(max_length=CAT_NAME_MAX_LENGTH)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name