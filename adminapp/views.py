from Tools.scripts.which import msg
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Admin,Student,Course,faculty,FacultyCourseMapping
from .forms import addFacultyForm,addStudentForm

# Create your views here.
def adminhome(request):
    aname = request.session['aname']
    return render(request,'adminhome.html',{'adminname':aname})
def changepassword(request):
    aname = request.session['aname']
    return render(request,'changepassword.html',{'adminname':aname})
def adminupdatepwd(request):
    aname = request.session['aname']
    opwd=request.POST['opwd']
    npwd=request.POST['npwd']
    flag=Admin.objects.filter(Q(username=aname)& Q(password=opwd))
    if flag:
        print("password is correct")
        Admin.objects.filter(username=aname).update(password=npwd)
        print("update successfully.....")
        msg="Password update successfully....."
    else:
        print("wrong password")
        msg = "Password update Failed....."
    return render(request,'changepassword.html',{'msg':msg,'adminname':aname})


def facultycoursemapping(request):
    aname = request.session['aname']
    fmcourse=FacultyCourseMapping.objects.all()
    return render(request,'facultycoursemapping.html',{'adminname':aname,'fmcourse':fmcourse})
def adminlogout(request):
    return render(request,'about.html')

def adminlogin(request):
    adminname = request.POST.get('uname', '')
    adminpwd = request.POST.get('pwd', '')
    flag = Admin.objects.filter(Q(username=adminname) & Q(password=adminpwd))

    print(flag)

    if flag:
        print("login successful")
        request.session['aname']=adminname
        return render(request,'adminhome.html',{'adminname':adminname})
    else:
        msg='Username or Password Wrong'
        return render(request,'login.html',{'msg':msg})
        #return HttpResponse("login failed")

# def studenthome(request):
#     sname = request.session['sname']
#     return render(request,'studenthome.html',{'sname':sname})
# def checkstudentlogin(request):
#     studentname = request.POST.get('uname')
#     studentpwd = request.POST.get('pwd')
#     flag = Student.objects.filter(Q(studentid=studentname) & Q(password=studentpwd))
#
#     print(flag)
#
#     if flag:
#         print("login successful")
#         request.session['sname']=studentname
#         return render(request,'studenthome.html',{'studentname':studentname})
#     else:
#         msg='Login Failed'
#         return render(request,'studentlogin.html',{'msg':msg})

def viewstudent(request):
    aname = request.session['aname']
    student=Student.objects.all()
    count=Student.objects.count()
    return render(request,'viewstudent.html',{"studentlist":student,"count":count,"count":count,'adminname':aname})

def facultyhome(request):
    fname = request.session['fname']
    return render(request,'facultyhome.html',{'fname':fname})

def viewfaculty(request):
    aname = request.session['aname']
    faculties = faculty.objects.all()
    count = faculty.objects.count()
    return render(request,'viewfaculty.html',{"facultylist":faculties,"count":count,'adminname':aname})
def viewcourses(request):
    aname = request.session['aname']
    course = Course.objects.all().order_by('id')
    count = Course.objects.count()
    return render(request,'viewcourses.html',{"courselist":course,"count":count,'adminname':aname})

def admincourse(request):
    aname=request.session['aname']
    return render(request,'admincourse.html',{'adminname':aname})

def adminstudent(request):
    aname = request.session['aname']
    return render(request,'adminstudent.html',{'adminname':aname})

def adminfaculty(request):
    aname = request.session['aname']
    return render(request,'adminfaculty.html',{'adminname':aname})

def checkfacultylogin(request):
    faultyname = request.POST.get('uname')
    facultypwd = request.POST.get('pwd')
    flag = faculty.objects.filter(Q(facultyid=faultyname) & Q(password=facultypwd))

    print(flag)

    if flag:
        print("login successful")
        request.session['fname']=faultyname
        return render(request,'facultyhome.html',{'facultyname':faultyname})
    else:
        msg='Username or Password Wrong'
        return render(request,'facultylogin.html',{'msg':msg})

def addcourse(request):
    aname = request.session['aname']
    return render(request,'addcourse.html',{'adminname':aname})
def addstudent(request):
    aname = request.session['aname']
    form = addStudentForm()
    if request.method == "POST":
        form1 = addStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            message = "Student added sucessfully"
            return render(request, 'addstudent.html', {'msg': message, 'form': form,'adminname':aname})
        else:
            message = "Student added Failed"
            return render(request, 'addstudent.html', {'msg': message, 'form': form, 'adminname': aname})
    return render(request, 'addstudent.html', {'form': form,'adminname':aname})

def deletestudent(request):
    aname = request.session['aname']
    stu = Student.objects.all().order_by('studentid')
    count = Student.objects.count()
    return render(request, 'deletestudent.html', {"studentlist": stu, "count": count,'adminname':aname})


def studentdelete(request,studentid):
    st = Student.objects.get(id=studentid)
    st.delete()
    return redirect("deletestudent")

def updatestudent(request):
    aname = request.session['aname']
    fac = faculty.objects.all().order_by('id')
    count = faculty.objects.count()
    return render(request, 'updatestudent.html', {"studentlist": fac, "count": count,'adminname':aname})



def addfaculty(request):
    aname = request.session['aname']

    form=addFacultyForm()
    if request.method=="POST":
        form1=addFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="faculty added sucessfully"
            return render(request,'addfaculty.html',{'msg':message,'form':form,'adminname':aname})
        else:
            message = "faculty added failed"
            return render(request, 'addfaculty.html', {'msg': message, 'form': form, 'adminname': aname})

    return render(request,'addfaculty.html',{'form':form,'adminname':aname})

def deletefaculty(request):
    aname = request.session['aname']
    fac = faculty.objects.all().order_by('facultyid')
    count = faculty.objects.count()
    return render(request, 'deletefaculty.html', {"facultylist": fac, "count": count,'adminname':aname})


def facultydelete(request,facultyid):

    st = faculty.objects.get(id=facultyid)
    st.delete()
    return redirect("deletefaculty")



def updatefaculty(request):
    aname = request.session['aname']
    fac = faculty.objects.all().order_by('id')
    count = faculty.objects.count()
    return render(request, 'updatefaculty.html', {"facultylist": fac, "count": count,'adminname':aname})




def insertcourse(request):
    aname = request.session['aname']
    if request.method=='POST':
        program=request.POST['program']
        dept=request.POST['dept']
        ay=request.POST['ay']
        sem=request.POST['sem']
        year=request.POST['year']
        ccode=request.POST['ccode']
        ctitle=request.POST['ctitle']
        ltps=request.POST['ltps']
        credits=request.POST['credits']

        course=Course(program=program,department=dept,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
        Course.save(course)
        message="Course inserted Successfully"

        return render(request,'addcourse.html',{'msg':message,'adminname':aname})

def deletecourse(request):
    aname = request.session['aname']
    course = Course.objects.all().order_by('id')
    count = Course.objects.count()
    return render(request, 'deletecourse.html', {"courselist": course, "count": count,'adminname':aname})


def coursedelete(request,cid):

    st = Course.objects.get(id=cid)
    st.delete()
    return redirect("deletecourse")

def updatecourse(request):
    aname = request.session['aname']
    course = Course.objects.all().order_by('id')
    count = Course.objects.count()
    return render(request, 'adminupdatecourse.html', {"courselist": course, "count": count,'adminname':aname})

def courseupdate(request,cid):
    aname = request.session['aname']
    return render(request,'courseupdate.html',{'cid':cid,'adminname':aname})

def updatecourse_by_id(request):
    aname = request.session['aname']
    cid=request.POST['cid']
    coid=int(cid)
    program = request.POST['program']
    dept = request.POST['dept']
    ay = request.POST['ay']
    sem = request.POST['sem']
    year = request.POST['year']
    ccode = request.POST['ccode']
    ctitle = request.POST['ctitle']
    ltps=request.POST['ltps']
    credits = request.POST['credits']

    Course.objects.filter(id=coid).update(program=program,department=dept,academicyear=ay,semester=sem,year=year,coursetitle=ctitle,ltps=ltps,credits=credits)
    msg="Course Updated Successfully"
    return render(request,'courseupdate.html',{'msg':msg,'adminname':aname,'cid':cid})