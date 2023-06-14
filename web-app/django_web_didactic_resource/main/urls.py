from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('generate_task/', views.generate_tasks, name = 'create_tasks'),
    path('generate_task/generated_tasks', views.generated_tasks, name = 'generated_task'),
    path('all_tasks/', views.reg, name = 'all_tasks'),
    path('account/', views.generate_tasks, name = 'account'),
    path('kid_generate_task/', views.kid_generate_tasks, name = 'kid_create_tasks'),
    path('kid_generate_task/tested', views.my_view, name = 'test'),
]