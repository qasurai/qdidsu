from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *

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

def getrealname(u,c):
    for i in u:
        if i[1]==c:
            return i[0]

def index(request):
    return render(request,"index.html")

def reg(request):
    obj=None
    if request.method=="GET":
        return render(request,"reg.html")
    else:
        try:
            name=request.POST.get("name")
            college=request.POST.get("college")
            grade=request.POST.get("grade")
            mentor=request.POST.get("mentor")
            is_active=True if request.POST.get("is_active")=="是" else False
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
            obj=Representative.objects.create(
                name=name,
                college=getrealname(college_u,college),
                grade=getrealname(grade_u,grade),
                mentor=getrealname(mentor_u,mentor),
                studentnumber=studentnumber,is_active=is_active,
            )
            obj.save()
        except Exception as e:
            messages.add_message(request, messages.ERROR,e)
            return render(request,"reg.html")
        messages.add_message(request, messages.SUCCESS,"注册成功")
        request.session["iflog"]='on'
        request.session["rid"]=obj.id
        return redirect('/list/')
        # return render(request,"reg.html")
    
def getlist(request):
    if(request.session.get('iflog')=='on'):
        obj=Proposal.objects.filter(
            forrep=Representative.objects.get(id=request.session['rid'])
        )
        obj1=Proposal.objects.filter(
            forrep_1=Representative.objects.get(id=request.session['rid'])
        )
        obj2=Proposal.objects.filter(
            forrep_2=Representative.objects.get(id=request.session['rid'])
        )
        obj3=Proposal.objects.filter(
            forrep_3=Representative.objects.get(id=request.session['rid'])
        )
        obj1=obj1|obj2|obj3
        return render(request,"list.html",locals())
    else:
        return redirect('/login/')

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        try:
            name=request.POST.get("name")
            college=request.POST.get("college")
            grade=request.POST.get("grade")
            mentor=request.POST.get("mentor")
            studentnumber=int(request.POST.get("studentnumber"))
            if len(name)>20:
                messages.add_message(request, messages.ERROR,'姓名不超过20个字符')
                return render(request,"login.html")
            if college not in college_c:
                messages.add_message(request, messages.ERROR,'学院不存在')
                return render(request,"login.html")
            if grade not in grade_c:
                messages.add_message(request, messages.ERROR,'年级不存在')
                return render(request,"login.html")
            if mentor not in mentor_c:
                messages.add_message(request, messages.ERROR,'导师不存在')
                return render(request,"login.html")
            if not (10000000<studentnumber and studentnumber<=99999999):
                messages.add_message(request, messages.ERROR,'学号不合法')
                return render(request,"login.html")
            obj=Representative.objects.filter(
                name=name,
                college=getrealname(college_u,college),
                grade=getrealname(grade_u,grade),
                mentor=getrealname(mentor_u,mentor),
                studentnumber=studentnumber,
            )
            if obj:
                request.session['iflog']="on"
                request.session['rid']=obj[0].id
                messages.add_message(request, messages.SUCCESS,"登录成功")
                return redirect("/list/")
            else:
                messages.add_message(request, messages.ERROR,"信息错误")
                return render(request,"login.html")
        except Exception as e:
            messages.add_message(request, messages.ERROR,e)
            return render(request,"login.html")
        
def logout(request):
    request.session['iflog']="off"
    return redirect("/")

def viewp(request,uid):
    if(request.session.get('iflog')=='on'):
        obj=Proposal.objects.get(id=uid)
        userobj=Representative.objects.get(id=request.session['rid'])
        if obj.forrep==userobj or obj.forrep_1==userobj or obj.forrep_2==userobj or obj.forrep_3==userobj: 
            return render(request,"view.html",locals())
        else:
            return redirect("/list/")
    else:
        return redirect('/login/')

def delgl(request,uid):
    if(request.session.get('iflog')=='on'):
        obj=Proposal.objects.get(id=uid)
        userobj=Representative.objects.get(id=request.session['rid'])
        if obj.forrep_1==userobj:
            obj.forrep_1=None
            obj.save()
            messages.add_message(request, messages.SUCCESS,"取消关联成功")
            return redirect('/list/')
        if obj.forrep_2==userobj:
            obj.forrep_2=None
            obj.save()
            messages.add_message(request, messages.SUCCESS,"取消关联成功")
            return redirect('/list/')
        if obj.forrep_3==userobj:
            obj.forrep_3=None
            obj.save()
            messages.add_message(request, messages.SUCCESS,"取消关联成功")
            return redirect('/list/')
    else:
        return redirect('/login/')

def delp(request,uid):
    if(request.session.get('iflog')=='on'):
        obj=Proposal.objects.get(id=uid)
        userobj=Representative.objects.get(id=request.session['rid'])
        if obj.forrep==userobj:
            obj.delete()
            messages.add_message(request, messages.SUCCESS,"删除成功")
            return redirect("/list/")
        else:
            return redirect("/list/")
    else:
        return redirect('/login/')
    
def add(request):
    if(request.session.get('iflog')=='on'):
        userobj=Representative.objects.get(id=request.session['rid'])
        if request.method=="GET":
            return render(request,"add.html")
        else:
            title=request.POST.get("title")
            obj=Proposal.objects.create(title=title,forrep=userobj)
            return redirect('/edit/{}/'.format(obj.id))
    else:
        return redirect('/login/')
    
def edit(request,uid):
    if(request.session.get('iflog')=='on'):
        obj=Proposal.objects.get(id=uid)
        userobj=Representative.objects.get(id=request.session['rid'])
        if obj.forrep==userobj:
            if request.method=="GET":
                return render(request,'edit.html',locals())
            else:
                try:
                    title=request.POST.get("title")
                    forrep_1=Representative.objects.get(studentnumber=int(request.POST.get("forrep_1"))) if request.POST.get("forrep_1") else None
                    forrep_2=Representative.objects.get(studentnumber=int(request.POST.get("forrep_2"))) if request.POST.get("forrep_2") else None
                    forrep_3=Representative.objects.get(studentnumber=int(request.POST.get("forrep_3"))) if request.POST.get("forrep_3") else None
                    reason=request.POST.get("reason")
                    solvetion=request.POST.get("solvetion")
                    obj.title=title
                    obj.forrep_1=forrep_1
                    obj.forrep_2=forrep_2
                    obj.forrep_3=forrep_3
                    obj.reason=reason
                    obj.solvetion=solvetion
                    obj.save()
                    messages.add_message(request, messages.SUCCESS,"修改成功")
                    return redirect("/view/{}/".format(obj.id))
                except Exception as e:
                    messages.add_message(request,messages.ERROR,e)
                    return render(request,"edit.html")
        else:
            return redirect("/list/")
    else:
        return redirect('/login/')
