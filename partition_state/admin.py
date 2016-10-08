from django.contrib import admin

# Register your models here.
from .models import t_apk_system_config


class t_apk_system_configAdmin(admin.ModelAdmin):
	fields = ['project', 'version', 'systemsize', 'fixedsize', 'surplussize']
	list_display = ('project', 'version', 'systemsize', 'fixedsize', 'surplussize')
	list_filter = ['project']
	search_fields = ['project', 'version']

admin.site.register(t_apk_system_config, t_apk_system_configAdmin)
