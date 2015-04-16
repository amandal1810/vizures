from django.shortcuts import render, render_to_response, get_object_or_404,get_list_or_404
from rat.models import Student,Semester,Marks
from django.http import HttpResponse
import datetime
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#views for home page
def home(request):
    return render(request,'rat/home.html',{})


#return a dictionary using information of a student object
def get_student_obj(i,rk):
        return {'rank':rk+1,'reg_no':i.reg_no, 'name': i.name, 'roll_no':i.roll_no, 'cgpa': i.cgpa}
    

def get_department_rankings(department_name):
    
    regex= '\d\d/'+department_name+'/*'
    dp_ranks= [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    
    if dp_ranks== 'CH':
        regex= '\d\d/CHE/*'
        dp_ranks+=  [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    
    return dp_ranks


college_ranks= [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.order_by('-cgpa').all()) ]

department_ranks={'CS': get_department_rankings('CS'),
                  'EC': get_department_rankings('EC'),
                  'EE': get_department_rankings('EE'),
                  'ME': get_department_rankings('ME'),
                  'MM': get_department_rankings('MM'),
                  'IT': get_department_rankings('IT'),
                  'CH': get_department_rankings('CH'),
                  'BT': get_department_rankings('BT'),}

def personal(request):
    inp = request.POST.get('roll')
    #data = Student.objects.get(reg_no=inp)
    marks= get_list_or_404(Marks,reg_no=inp)
#    marks= Marks.objects.get_object_404(reg_no=inp)
    
    print marks
    
    if marks == None:
        print "SOMETHING BAD HAPPENED"
        return render(request,'rat/personal_profile.html')
        
    #print marks.reg_no.name
    
    college_rank=0
    department_rank=0
    
    for i in college_ranks:
        if i['reg_no']== int(inp):
            college_rank= i['rank']
    
    department= 'CS'
    
    if 'CS' in marks[0].reg_no.roll_no:
        department= 'CS'
    
    if 'CH' in marks[0].reg_no.roll_no:
        department= 'CH'
    
    if 'EC' in marks[0].reg_no.roll_no:
        department= 'EC'
    
    if 'EE' in marks[0].reg_no.roll_no:
        department= 'EE'
        
    if 'EE' in marks[0].reg_no.roll_no:
        department= 'EE'
        
    if 'ME' in marks[0].reg_no.roll_no:
        department= 'ME'
        
    if 'MM' in marks[0].reg_no.roll_no:
        department= 'MM'
        
    if 'BT' in marks[0].reg_no.roll_no:
        department= 'BT'
        
    if 'IT' in marks[0].reg_no.roll_no:
        department= 'IT'
    
    
    print department
    
    inp = int(inp)
    
    print inp
    
    print inp.__class__
    
    department_rank_list= department_ranks[department]
    
    for i in department_rank_list:
        print i.__class__
        print i['reg_no'].__class__
        print i['reg_no']
        if i['reg_no']== inp:
            department_rank= i['rank']
            print "dep: ",department_rank
            break
    
    #dic = {'name':marks.reg_no.name,'roll':marks.reg_no.roll_no,'cgpa':marks.reg_no.cgpa,
    #       'college_ranking': college_rank, 'semester':marks.sem.sem/100,'marks':marks,
    #       }
    dic= {'marks':marks,'college_rank':college_rank,'department_rank':department_rank}
    return render(request,'rat/personal_profile.html', dic)
    

def college_ranking(request):
    rk=0
    #ranks= [get_student_obj(i,rk) for rk,i in enumerate(Student.objects.order_by('-cgpa').all())]
    paginator = Paginator(college_ranks,20)
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
    
    global department_ranks
    #inp = request.POST.get('department')
    print "department",dept_id
    which_department= dept_id
    
    if which_department== None:
        #which_department= 'CS'
        dic={'ranks':[]}
        return render(request,'rat/department_ranking.html',dic)
    
    regex= '\d\d/'+which_department+'/*'
    department_ranks= [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    
    if department_ranks== 'CH':
        regex= '\d\d/CHE/*'
        department_ranks+=  [ get_student_obj(i,rk) for rk,i in enumerate(Student.objects.filter(roll_no__regex= regex).order_by('-cgpa'))]
    
    dept={'CS':'Computer Science and Engineering',
          'EC': 'Electronics and Communications Engineering',
          'ME': 'Mechanical Engineering',
          'MM': 'Metallurgical and Materials Engineering',
          'CH': 'Chemical Engineering',
          'BT':'Biotechnology',
          'EE':'Electrical Engineering',
          'IT':'Information Technology',
          'CE':'Civil Engineering'}
    dic = {'ranks': department_ranks, 'department': dept[which_department]}
    return render(request,'rat/department_ranking.html',dic)

def personal_profile(request):
    #return HttpResponse('personal_profile')
    return render(request,'rat/personal_profile.html',{})

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)
