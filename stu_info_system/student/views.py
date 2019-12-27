from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *

def home(request):
	if request.session.get('user'):
		del request.session['user']
	return render(request, "index.html")

def slogin(request):
	if request.method == 'GET':
		return render(request, "login.html")
	
	if request.method == "POST":
		name = request.POST.get('user')
		password = request.POST.get("password")
		if STUDENT.objects.filter(STUDENTID=int(name)).exists():
			user = STUDENT.objects.get(STUDENTID=int(name))
			if password == user.PASSWD:
				info = STUDENT.objects.get(STUDENTID=int(name)

)
				request.session['user'] = user.STUDENTID
				return render(request, "stuinfo.html",{"stu": info})
			else:
				return render(request, "login.html", {"error": "密码错误"})
		else:
			return render(request, "login.html",{"error":  "用户不存在"})

def modify(request):
	if request.session.get('user'):
		return render(request, "modify.html")
	else:
		return HttpResponse("请登录后操作")

def slogout(request):
	if request.session.get('user'):
		del request.session['user']
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
# Create your views here.
