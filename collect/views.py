from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import csv,time,codecs

# Create your views here.

college_c=(
    'Lyceum'
    'Parnassus'
    'Virtus'
)
grade_c=(
    'G9'
    'G10'
    'G11'
    'G12'
)
mentor_c=(
    '郭俊卿'
    '赵胡梦鹤'
    '刘芳雨'
    '王倩宇'
    '赵航'
    '高行健'
    '王思洋'
    '朱宝杰'
    '周芳颖'
    '孙莹莹'
    '赵昊一'
    '李帅'
    '兰文稚'
    '王一童'
    '李肖阳'
    '于晓冬'
    '苏盼文'
    '王菁'
    '李妍'
    '邢文娟'
    '王乃伟'
    '徐颖雪'
    '于江'
    '林帅'
)

def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method=="GET":
        return render(request,"reg.html")
    else:
        try:
            name=request.POST.get("name")
            college=request.POST.get("college")
            grade=request.POST.get("grade")
            mentor=request.POST.get("mentor")
            content=request.POST.get("content")
            studentnumber=int(request.POST.get("studentnumber"))
            if len(name)>20:
                messages.add_message(request, messages.ERROR,'姓名不超过20个字符')
                return render(request,"reg.html")
            if college not in college_c:
                messages.add_message(request, messages.ERROR,'学院不存在')
                return render(request,"reg.html")
            if grade not in grade_c:
                messages.add_message(request, messages.ERROR,'年级不存在')
                return render(request,"reg.html")
            if mentor not in mentor_c:
                messages.add_message(request, messages.ERROR,'导师不存在')
                return render(request,"reg.html")
            if not (10000000<studentnumber and studentnumber<=99999999):
                messages.add_message(request, messages.ERROR,'学号不合法')
                return render(request,"reg.html")
            Representative.objects.create(
                name=name,
                college=college,
                grade=grade,
                mentor=mentor,
                studentnumber=studentnumber,
                content=content,
            ).save()
        except Exception as e:
            messages.add_message(request, messages.ERROR,e)
            return render(request,"reg.html")
        messages.add_message(request, messages.SUCCESS,"注册成功")
        return render(request,"reg.html")

def getcsv(request):
    stu_lis = Representative.objects.all()
    response = HttpResponse(content_type='text/csv', charset='UTF-8')
    time_now = time.strftime('%Y%m%d')
    filename = 'QAIDSRM_' + time_now
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(['Id','name','college','grade','mentor','studentnumber','content'])
    for stu in stu_lis:
        writer.writerow([stu.id,stu.name,stu.college,stu.grade,stu.mentor,stu.studentnumber,stu.content])
    return response