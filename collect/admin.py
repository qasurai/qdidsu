from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from .models import *
import csv,time,codecs

# Register your models here.
class RepresentativeAdmin(admin.ModelAdmin):
	list_display = ['id','name','college','grade','mentor','content','create_data','last_change_data','is_active']
	list_filter = ['college','grade','mentor']
	actions = ['export']
	def export(self,request,queryset):
		alldata = queryset
		response = HttpResponse(content_type='text/csv', charset='UTF-8')
		time_now = time.strftime('%Y%m%d_%H_%M_%S')
		filename = 'Representative_' + time_now
		response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
		response.write(codecs.BOM_UTF8)
		writer = csv.writer(response)
		writer.writerow(['Id','name','college','grade','mentor','studentnumber','create_data','last_change_data'])
		for i in alldata:
			writer.writerow([i.id,i.name,i.get_college_display(),i.get_grade_display(),i.get_mentor_display(),i.studentnumber,i.create_data,i.last_change_data])
		return response
admin.site.register(Representative,RepresentativeAdmin)

template_proposal='''### {} {}

> 提案人: {}
>
> 附议人: {} {} {}

#### 提案缘由
{}
#### 解决发难
{}
#### 初审意见
> {}

'''

class ProposalAdmin(admin.ModelAdmin):
	list_display = ['id','init_views','init_opinion','forrep','title','result','create_data','last_change_data']
	list_filter = ['init_views','result']
	actions = ['ExportToCsv','ExportToMarkDown']
	def ExportToCsv(self,request,queryset):
		stu_lis = queryset
		response = HttpResponse(content_type='text/csv', charset='UTF-8')
		time_now = time.strftime('%Y%m%d_%H_%M_%S')
		filename = 'Proposal_' + time_now
		response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
		response.write(codecs.BOM_UTF8)
		writer = csv.writer(response)
		writer.writerow(['Id','uid','init_views','init_opinion','forrep','forrep_1','forrep_2','forrep_3','title','reason','solvetion','result','create_data','last_change_data'])
		for stu in stu_lis:
			writer.writerow([stu.id,stu.uid,stu.init_views,stu.init_opinion,stu.forrep,stu.forrep_1,stu.forrep_2,stu.forrep_3,stu.title,stu.reason,stu.solvetion,stu.result,stu.create_data,stu.last_change_data])
		return response
	def ExportToMarkDown(self,request,queryset):
		stu_lis = queryset
		response = HttpResponse(content_type='text/plain', charset='UTF-8')
		time_now = time.strftime('%Y%m%d_%H_%M_%S')
		filename = 'Proposal_' + time_now
		response['Content-Disposition'] = f'attachment; filename="{filename}.md"'
		response.write(codecs.BOM_UTF8)
		writer = csv.writer(response)
		for stu in stu_lis:
			if stu.init_views:
				writer.writerows(template_proposal.format(
					stu.uid,stu.title,stu.forrep,stu.forrep_1,stu.forrep_2,stu.forrep_3,stu.reason,stu.solvetion,stu.init_opinion
				).strip("\n"))
		return response
admin.site.register(Proposal,ProposalAdmin)

class NewsAdmin(admin.ModelAdmin):
	list_display = ['id','title','content','create_data']
admin.site.register(News,NewsAdmin)

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['action_time','user','content_type','object_id','object_repr','action_flag','change_message']
admin.site.register(LogEntry,LogEntryAdmin)

class SessionAdmin(admin.ModelAdmin):
	list_display = ['session_key','session_data','expire_date']
admin.site.register(Session,SessionAdmin)

admin.site.site_title="Qingdao Academy International Department Student Congress。"
admin.site.site_header="Qingdao Academy International Department Student Congress."