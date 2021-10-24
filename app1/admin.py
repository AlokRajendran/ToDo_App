from django.contrib import admin

from .models import *

admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(Notification)

# Register your models here.
