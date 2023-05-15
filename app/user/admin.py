from django.contrib import admin
from .models import Sleep, StruggleDuration, Improvement, UserProfile


class SleepAdmin(admin.ModelAdmin):
    list_display = ['id']


class StruggleDurationAdmin(admin.ModelAdmin):
    list_display = ['id', 'sleep', 'duration']


class ImprovementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sleep', 'user', 'improvement']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'efficiency', 'sleep_hours',
                    'sleep_time', 'wakeup_time', 'sleep_improvement']
    list_filter = ['efficiency']
    search_fields = ['user__username']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Sleep, SleepAdmin)
admin.site.register(StruggleDuration, StruggleDurationAdmin)
admin.site.register(Improvement, ImprovementAdmin)
