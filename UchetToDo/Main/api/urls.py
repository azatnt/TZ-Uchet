from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('todo/', AllTasks.as_view(), name='all_tasks_url'),
    path('todo/<int:id>', TaskDetail.as_view(), name='task_detail_url'),
    path('todo/<int:id>/execute/', TaskExecute.as_view(), name='task_execute_url'),
    path('register', Register.as_view(), name="register_url"),
    path('login', obtain_auth_token, name="login_url"),
    path('user_update', UpdateUser.as_view(), name="change_user_url"),
    path('logout', Logout.as_view(), name="logout_url"),


]
