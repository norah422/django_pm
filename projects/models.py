from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')


class Project_status(models.IntegerChoices):
    PENDING = 1, _('pending')
    COMPLETED = 2, _('completed')
    POSTPONED = 3, _('postponed')
    CANCELED = 4, _('canceled')


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.IntegerField(
        choices=Project_status.choices,
        default=Project_status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Project')

class Task(models.Model):
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Task')