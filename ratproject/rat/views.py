from django.shortcuts import render, render_to_response, get_object_or_404
from rat.models import Student,Semester,Marks
from django.http import HttpResponse
import datetime
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#related to data


def home(request):
    return render(request,'rat/home.html',{})


def get_student_obj(i,rk):
        return {'rank':rk+1,'reg_no':i.reg_no, 'name': i.name, 'roll_no':i.roll_no, 'cgpa': i.cgpa}
    

ranks= [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.order_by('-cgpa').all()) ]

def personal(request):
    inp = request.POST.get('roll')
    #data = Student.objects.get(reg_no=inp)
    marks= get_object_or_404(Marks,reg_no=inp)
#    marks= Marks.objects.get_object_404(reg_no=inp)
    
    if marks == None:
        return render(request,'rat/personal_profile.html')
        
    print marks.reg_no.name
    
    college_rank=0
    
    for i in ranks:
        if i['reg_no']== int(inp):
            college_rank= i['rank']
    
    print college_rank
    
    dic = {'name':marks.reg_no.name,'roll':marks.reg_no.roll_no,'cgpa':marks.reg_no.cgpa,
           'college_ranking': college_rank,
           }
    return render(request,'rat/personal_profile.html', dic)

def college_ranking(request):
    rk=0
    #ranks= [get_student_obj(i,rk) for rk,i in enumerate(Student.objects.order_by('-cgpa').all())]
    paginator = Paginator(ranks,20)
    page= request.GET.get('page')
    try:
        rank_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rank_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rank_page = paginator.page(paginator.num_pages)

    
    dic = {"ranks": rank_page}
    return render(request,'rat/college_ranking.html',dic)

def department_ranking(request,dept_id):
    
    #inp = request.POST.get('department')
    print "department",dept_id
    which_department= dept_id
    
    if which_department== None:
        #which_department= 'CS'
        dic={'ranks':[]}
        return render(request,'rat/department_ranking.html',dic)
    
    regex= '\d\d/'+which_department+'/*'
    ranks= [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    
    if ranks== 'CH':
        regex= '\d\d/CHE/*'
        ranks+=  [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    dic = {'ranks': ranks, 'department': which_department}
    return render(request,'rat/department_ranking.html',dic)

def personal_profile(request):
    #return HttpResponse('personal_profile')
    return render(request,'rat/personal_profile.html',{})

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
