from django.contrib import admin
from projects.models import Category, Project, Task

admin.site.register(Category),
admin.site.register(Project),
admin.site.register(Task)