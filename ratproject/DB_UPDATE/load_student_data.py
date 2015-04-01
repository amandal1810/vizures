# Full path and name to your csv file



base_dir = os.path.dirname(__file__)

csv_filepathname=os.path.join(base_dir,"csv/student_file.csv")



# Full path to your django project directory

your_djangoproject_home=os.path.dirname(os.path.dirname(__file__))


import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()
 
from dbUpgrade.models import Student 
import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:        
    student=Student()
    student.reg_no = row[0]
    student.roll_no = row[1]
    student.name = row[2]
    student.department = row[3]
    print( row[4] )
    student.cgpa= float(row[4])
    
    student.save()
