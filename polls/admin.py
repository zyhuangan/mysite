from django.contrib import admin

# Register your models here.

from .models import Question,t_apk_system_config

admin.site.register(Question)
admin.site.register(t_apk_system_config)
