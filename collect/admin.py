from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from .models import *

# Register your models here.
class RepresentativeAdmin(admin.ModelAdmin):
	list_display = ['id','name','college','grade','mentor','content','create_data','last_change_data','is_active']
	list_filter = ['college','grade','mentor']
admin.site.register(Representative,RepresentativeAdmin)

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['action_time','user','content_type','object_id','object_repr','action_flag','change_message']
admin.site.register(LogEntry,LogEntryAdmin)

class SessionAdmin(admin.ModelAdmin):
	list_display = ['session_key','session_data','expire_date']
admin.site.register(Session,SessionAdmin)

admin.site.site_title="Student Representative Meeting"
admin.site.site_header="Student Representative Meeting"