from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.Project_list_view.as_view(), name='Project_list'),
    path('project/create', views.Project_creat_view.as_view(), name='Project_create'),
]
