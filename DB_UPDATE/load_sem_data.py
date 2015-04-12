# Full path and name to your csv file

import sys
import os

base_dir = os.path.dirname(__file__)
# Full path to your django project directory

your_djangoproject_home=os.path.dirname(os.path.dirname(__file__))
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ratproject.settings'

import django
django.setup()


dir_name= 'csv'

file_names= os.listdir(dirname)


for file_name in file_names:

    path_name= dirname+'/'+file_name
    csv_filepathname=os.path.join(base_dir,path_name)

     
    from rat.models import Student,Semester,Marks
     
    import csv
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    i=0
    sem=Semester()
    for row in dataReader:
            
            if i==0:        
                    sem.sem = row[0]
                    sem.sub1 = row[1]
                    sem.sub2 = row[2]
                    sem.sub3 = row[3]
                    sem.sub4 = row[4]
                    sem.sub5 = row[5]
                    sem.lab1 = row[6]
                    sem.lab2 = row[7]
                    sem.lab3 = row[8]
                    sem.save()
                    i=1
            else:
            	marks=Marks()
            	student=Student.objects.get(pk=row[0])
            	print ("%d  %s  %s  %s  %f" %(student.reg_no,student.roll_no,student.name,student.department,student.cgpa))
            	student.cgpa=float(row[31])
            	
            	marks.reg_no=student
            	
            	marks.sem=sem
            	marks.sub1=row[4]
            	marks.sub2=row[7]
            	marks.sub3=row[10]
            	marks.sub4=row[13]
            	marks.sub5=row[16]
            	marks.lab1=row[19]
            	marks.lab2=row[22]
            	marks.lab3=row[25]
            	marks.sgpa=float(row[28])
            	marks.cgpa=float(row[31])
            	marks.sem_credits=row[27]
            	marks.total_credits=row[30]
            	marks.remarks=row[32]

            	student.save()

            	marks.save()
        	
