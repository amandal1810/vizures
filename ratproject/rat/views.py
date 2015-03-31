from django.shortcuts import render
from rat.models import Student
# Create your views here.

def home(request):
    return render(request,'rat/home.html',{})

def process(request):
    inp = request.POST.get('roll')
    data = Student.objects.get(roll=inp)
    dic = {'name':data.name,'roll':data.roll,'cgpa':data.cgpa}
    return render(request,'rat/result.html', dic)
