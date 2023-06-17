from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    username = models.CharField('Username', max_length=25)
    name = models.CharField('Имя', max_length=25)
    surname = models.CharField('Фамилия', max_length=25)
    password = models.CharField('Пароль')
    email = models.CharField('Почта')
    access_t = models.BooleanField('Доступ')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

class Classes(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    class_lit= models.CharField('Lit', max_length=2)
    class_num = models.IntegerField('Номер класса')

    def __str__(self):
        return str(self.class_num) + ' ' + str(self.class_lit)

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Student(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    person_id = models.ForeignKey("Person", on_delete=models.CASCADE)
    class_id = models.ForeignKey("Classes", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) +' '+ str(self.person_id)+ ' ' + str(self.class_id)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Teacher(models.Model):
    id = models.PositiveIntegerField(default=0, primary_key=True)
    person_id = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person_id)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Task_shablon(models.Model):
    theme = models.CharField('Theme', max_length=25)
    task = models.CharField('Task', max_length=350)

    def __str__(self):
        return str(self.theme) + ' ' + str(self.task)

    class Meta:
        verbose_name = "Шаблон задания"
        verbose_name_plural = "Шаблоны заданий"


class Obj_shablon(models.Model):
    theme = models.CharField('Theme', max_length=25)
    name = models.CharField('Name_obj', max_length=20)
    min_value = models.IntegerField(default=1)
    max_value = models.IntegerField(default=100)
    unit1 = models.CharField('Unit1', max_length=15)
    max_s = models.IntegerField(default=500)
    unit2 = models.CharField('Task', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Шаблон объекта"
        verbose_name_plural = "Шаблоны объектов"


class Info_about_task(models.Model):
    shablon_id = models.ForeignKey("Task_shablon", on_delete=models.CASCADE)
    obj_id = models.ForeignKey("Obj_shablon", on_delete=models.CASCADE, default='')

    def __str__(self):
        return str(self.shablon_id) + ' ' + str(self.obj_id)

    class Meta:
        verbose_name = "Информация о задании"
        verbose_name_plural = "Информация о заданиях"


class Comon_task(models.Model):
    class_id = models.ForeignKey("Classes", on_delete=models.CASCADE)
    teacher_id = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата создания задания")
    info_task_id = models.ForeignKey("Info_about_task", on_delete=models.CASCADE)
    document = models.FileField(default='')

    def __str__(self):
        return str(self.class_id) + str(self.teacher_id) + str(self.info_task_id)

    class Meta:
        verbose_name = "Обычное задание"
        verbose_name_plural = "Обычные задания"


class Individual_task(models.Model):
    student_id = models.ForeignKey("Student", on_delete=models.CASCADE)
    teacher_id = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата создания задания")
    info_task_id = models.ForeignKey("Info_about_task", on_delete=models.CASCADE)
    document = models.FileField(default='')

    def __str__(self):
        return str(self.student_id) + str(self.teacher_id) + str(self.info_task_id)

    class Meta:
        verbose_name = "Индивидуальное задание"
        verbose_name_plural = "Индивидуальные задания"

class Tasks(models.Model):
    document = models.FileField(default='SOME STRING')
    answers = models.FileField(default='SOME STRING')
    uploaded_at = models.DateTimeField("Дата создания задания",default='')