from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.Project_list_view.as_view(), name='Project_list'),
    path('project/create', views.Project_creat_view.as_view(), name='Project_create'),
    path('project/edit/<int:pk>', views.Project_update_view.as_view(), name='Project_update'),
    path('project/delete/<int:pk>', views.Project_delete_view.as_view(), name='Project_delete'),
    path('task/create', views.Task_creat_view.as_view(), name='Task_create'),
    path('task/edit/<int:pk>', views.Task_update_view.as_view(), name='Task_update'),
    path('task/delete/<int:pk>', views.Task_delete_view.as_view(), name='Task_delete'),

]
