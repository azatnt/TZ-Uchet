from django.urls import path
from .views import *
from django.conf.urls import include


urlpatterns = [
    path('', base, name='base_url'),
    path('task/delete/<int:id>', delete_task, name='delete_task_url'),
    path('task/edit/<int:id>', edit_task, name='edit_taks_url'),
    path('task/update/<int:id>', update_task, name='update_task_url'),

]
