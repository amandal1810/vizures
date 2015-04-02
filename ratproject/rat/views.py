from django.shortcuts import render
from rat.models import Student
from django.http import HttpResponse
import datetime
from django.core.urlresolvers import reverse

# Create your views here.

def home(request):
    return render(request,'rat/home.html',{})

def get_absolute_url(self): 
    """Construct the absolute URL for this Item."""
    return reverse('project.app.views.view_name', None, [str(self.id)])

def process(request):
    inp = request.POST.get('roll')
    data = Student.objects.get(reg_no=inp)
    dic = {'name':data.name,'roll':data.reg_no,'cgpa':data.cgpa}
    return render(request,'rat/result.html', dic)

def college_ranking(request):    
    ranks= [str(i) for i in Student.objects.order_by('-cgpa').all()]
    print type(ranks[0]),ranks[0]
    #html= '<br>'.join(ranks)
    #html = '<ol>'+ html + '</ol>'
    #return HttpResponse(html)
    dic = {'ranks': ranks}
    return render(request,'rat/college_ranking.html',dic)

def department_ranking(request):
    
    def get_student_obj(i,rk):
        return {'rank':rk+1,'reg_no':i.reg_no, 'name': i.name, 'roll_no':i.roll_no, 'cgpa': i.cgpa}
    
    inp = request.POST.get('department')
    print "department",inp
    which_department= inp
    
    if which_department== None:
        #which_department= 'CS'
        dic={'ranks':[]}
        return render(request,'rat/department_ranking.html',dic)
    
    regex= '\d\d/'+which_department+'/*'
    ranks= [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    
    if ranks== 'CH':
        regex= '\d\d/CHE/*'
        ranks+=  [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    #html= '<br>'.join(ranks)
    #html = '<ol>'+ html + '</ol>'
    #return HttpResponse(html)
    dic = {'ranks': ranks, 'department': which_department}
    return render(request,'rat/department_ranking.html',dic)

def personal_profile(request):
    return HttpResponse('personal_profile')

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
