from django.contrib import admin
from .models import Student, Classes, Person, Task_shablon, Obj_shablon, Info_about_task, Individual_task, Comon_task, Teacher,Tasks
# Register your models here.

admin.site.register(Student)
admin.site.register(Classes)
admin.site.register(Person)
admin.site.register(Task_shablon)
admin.site.register(Obj_shablon)
admin.site.register(Info_about_task)
admin.site.register(Individual_task)
admin.site.register(Comon_task)
admin.site.register(Teacher)
admin.site.register(Tasks)