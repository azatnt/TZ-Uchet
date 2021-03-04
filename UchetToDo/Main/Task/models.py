from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




class Task(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    isDone = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
