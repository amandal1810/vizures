from django.db import models

# Create your models here.

class Student(models.Model):
    reg_no = models.IntegerField(primary_key=True,default='20120000')
    roll_no = models.CharField(max_length=10,default='')
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50,default= 'CSE')
    cgpa = models.DecimalField(max_digits=4,decimal_places=2)
    
    def __unicode__(self):
        return str(self.reg_no)+" "+self.name+" "+self.roll_no+" "+str(self.cgpa)
    
class Semester(models.Model):
    sem = models.IntegerField(primary_key=True)
    sub1 = models.CharField(max_length=50)
    sub2 = models.CharField(max_length=50)
    sub3 = models.CharField(max_length=50)
    sub4 = models.CharField(max_length=50)
    sub5 = models.CharField(max_length=50)
    lab1 = models.CharField(max_length=50)
    lab2 = models.CharField(max_length=50)
    lab3 = models.CharField(max_length=50)
    
    #def __unicode__(self):
    #    return str(self.sem)+" "+self.sub1+" "+self.sub2+" "+self.sub3+" "\
    #+self.sub4+" "+self.sub5+" "+ self.lab1+ " " + self.lab2+ " "+ self.lab3

class Marks(models.Model):
    reg_no = models.ForeignKey(Student)
    sem = models.ForeignKey(Semester)
    sub1 = models.IntegerField(default=0)
    sub2 = models.IntegerField(default=0)
    sub3 = models.IntegerField(default=0)
    sub4 = models.IntegerField(default=0)
    sub5 = models.IntegerField(default=0)
    lab1 = models.IntegerField(default=0)
    lab2 = models.IntegerField(default=0)
    lab3 = models.IntegerField(default=0)
    sgpa = models.DecimalField(max_digits=4,decimal_places=2)
    cgpa = models.DecimalField(max_digits=4,decimal_places=2)
    sem_credits = models.IntegerField(default=0)
    total_credits = models.IntegerField(default=0)
    remarks = models.CharField(max_length=10)
    
    def __unicode__(self):
        return str(self.sem)+" "+str(self.reg_no)+ " "+ str(self.sub1) +" "+str(self.sub2)+" "+str(self.sub3)+" "\
    + str(self.sub4)+" "+str(self.sub5)+" "+ str(self.lab1) + " " + str(self.lab2)+ " "+ str(self.lab3) + " "\
    + str(self.sgpa)+ " "+ str(self.cgpa)+ " "+ str(self.sem_credits)+ " "\
+ str(self.total_credits)+" "+ self.remarks


#class Student(models.Model):
#	name = models.CharField(max_length=60, blank=False)
#	roll = models.CharField(max_length=10, primary_key=True, blank=False)
#	cgpa = models.FloatField()
