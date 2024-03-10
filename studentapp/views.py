from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course


# Create your views here.
def studenthome(request):
    sname = request.session['sname']
    student=Student.objects.get(studentid=sname)
    return render(request,'studenthome.html',{'studentname':sname,'student':student})

def checkstudentlogin(request):
    studentname = request.POST.get('uname')
    studentpwd = request.POST.get('pwd')
    flag = Student.objects.filter(Q(studentid=studentname) & Q(password=studentpwd))

    print(flag)

    if flag:
        print("login successful")
        request.session['sname']=studentname
        student = Student.objects.get(studentid=studentname)
        return render(request,'studenthome.html',{'studentname':studentname,'student':student})
    else:
        msg='Username or Password Wrong'
        return render(request,'studentlogin.html',{'msg':msg})



def studentchangepassword(request):
    sname = request.session['sname']
    return render(request,'studentchangepassword.html',{'studentname':sname})
def studentupdatepwd(request):
    sname = request.session['sname']
    opwd=request.POST['opwd']
    npwd=request.POST['npwd']
    flag=Student.objects.filter(Q(studentid=sname)& Q(password=opwd))
    if flag:
        print("password is correct")
        Student.objects.filter(studentid=sname).update(password=npwd)
        print("update successfully.....")
        msg="student Password update successfully....."
    else:
        print("wrong password")
        msg = "Password update Failed....."
    return render(request,'studentchangepassword.html',{'msg':msg,'studentname':sname})

def studentcourses(request):
    sname = request.session['sname']
    return render(request,'studentcourses.html',{'studentname':sname})

def displaystudentcourses(request):
    sname = request.session['sname']
    ay=request.POST['ay']
    sem= request.POST['sem']
    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request,'displaystudentcourses.html',{'courses':courses,'studentname':sname})
