from django.urls import path, include
from . import views

app_name = 'app1'

urlpatterns = [
    
    path('', views.IndexView.as_view(), name= 'indexpage'),
    path('add_task', views.AddTask.as_view(), name= 'addtask'),
    path('add_tasktype', views.AddTaskType.as_view(), name= 'addtasktype')

]