from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    efficiency = models.IntegerField(null=True, blank=True)
    sleep_hours = models.IntegerField(null=True, blank=True)
    sleep_time = models.TimeField(null=True, blank=True)
    wakeup_time = models.TimeField(null=True, blank=True)
    sleep_improvement = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Sleep(models.Model):
    info = models.CharField(max_length=40)


class StruggleDuration(models.Model):
    sleep = models.ForeignKey(Sleep, on_delete=models.CASCADE)
    duration = models.CharField(max_length=255)


class Improvement(models.Model):
    sleep = models.ForeignKey(Sleep, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    improvement = models.CharField(max_length=255)
