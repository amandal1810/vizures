from django.shortcuts import render
from rat.models import Student
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    return render(request,'rat/home.html',{})

def process(request):
    inp = request.POST.get('roll')
    data = Student.objects.get(reg_no=inp)
    dic = {'name':data.name,'roll':data.reg_no,'cgpa':data.cgpa}
    return render(request,'rat/result.html', dic)

def college_ranking(request):    
    ranks= [str('<li>')+str(i)+str('</li>') for i in Student.objects.order_by('-cgpa').all()]
    print type(ranks[0]),ranks[0]
    html= '<br>'.join(ranks)
    html = '<ol>'+ html + '</ol>'
    return HttpResponse(html)

def department_ranking(request):
    which_department= 'CSE'
    ranks= [str('<li>')+str(i)+str('</li>') for i in Student.objects.filter(roll_no__regex=r'\d\d/CSE/*').order_by('-cgpa')]
    html= '<br>'.join(ranks)
    html = '<ol>'+ html + '</ol>'
    return HttpResponse(html)

def personal_profile(request):
    return HttpResponse('personal_profile')

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
