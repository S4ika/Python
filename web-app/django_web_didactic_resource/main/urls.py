from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('generate_task/', views.generate_tasks, name = 'create_tasks'),
    # path('generate_task/wtf', views.wtf, name = 'generated_tasks'),
    path('all_tasks/', views.reg, name = 'all_tasks'),
    path('account/', views.generate_tasks, name = 'account'),
    path('kid_generate_task/', views.kid_generate_tasks, name = 'kid_create_tasks'),
    path('kid_generate_task/tested', views.my_view, name = 'test'),
    path('generate_task/add/', views.add),
    path('generate_task/test2/', views.test),
    path('auth/log_in/', views.log_in),
    path('generate_task/add/upload', views.upload),
path('auth/log_in/create_tasks_kid', views.kid_generate_tasks),

]