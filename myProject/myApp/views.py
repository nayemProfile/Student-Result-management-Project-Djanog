from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *

def signUp(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object
            login(request, user)  # Log in the user after registration
            return redirect('homePage')  # Redirect to home page after signup
    else:
        form = UserCreateForm()
    
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def loginPage(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homePage")
            else:
                # Add an error message for invalid credentials
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()
    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)












def homePage(request):
    return render(request, 'home.html')


def studentAdd(request):
    student = Student_Model.objects.all()
    if request.method == "POST":
        form = Student_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentAdd')
    else:
        form = Student_Form()
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'studentAdd.html', context)

def studentDelete(request, id):
    s = Student_Model.objects.get(id=id)
    s.delete()
    return redirect("studentAdd")

def studentUpdate(request, id):
    students = Student_Model.objects.get(id = id)
    form = Student_Form(instance = students)
    if request.method=="POST":
        form = Student_Form(request.POST, instance = students)
        form.save()
        return redirect("studentAdd")
    return render(request, 'studentEdit.html',{'form':form} )






def subjectAdd(request):
    subject = Subject_Model.objects.all()
    if request.method == "POST":
        form = Subject_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subjectAdd")
    else:
        form = Subject_Form()
    context = {
        'form': form,
        'subject': subject
    }
    return render(request, 'subjectAdd.html', context)



def subjectDelete(request, id):
    s = Subject_Model.objects.get(id=id)
    s.delete()
    return redirect("subjectAdd")


def subjectUpdate(request, id):
    subject = Subject_Model.objects.get(id = id)
    form = Subject_Form(instance = subject)
    if request.method=="POST":
        form = Subject_Form(request.POST, instance = subject)
        form.save()
        return redirect("subjectAdd")
    return render(request, 'subjectEdit.html',{'form':form} )






def gradeAdd(request):
    grade = Grade_Model.objects.all()
    if request.method == "POST":
        form = Grade_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gradeAdd")
    else:
        form = Grade_Form()
    context = {
        'form': form,
        'grade': grade
    }
    return render(request,'grade.html', context)


def gradeDelete(request, id):
    g = Grade_Model.objects.get(id=id)
    g.delete()
    return redirect("gradeAdd")



def gradeUpdate(request, id):
    grade = Grade_Model.objects.get(id = id)
    form = Grade_Form(instance = grade)
    if request.method=="POST":
        form = Grade_Form(request.POST, instance = grade)
        form.save()
        return redirect("gradeAdd")
    return render(request, 'gradeEdit.html',{'form':form} )



def giveMark(request,id):
    student = Student_Model.objects.get(id = id)
    subject = Subject_Model.objects.all()
    
    if request.method == "POST":
        form = Grade_Form(request.POST)
        if form.is_valid():
            form.instance.student_model = student
            form.save()
            return redirect('gradeAdd')
    else:
        form = Grade_Form()
    context = {
        'form': form,
        'student': student,
        'subject': subject,
        
    }
    return render(request, 'giveMark.html', context)




def resultView(request, id):
    std = Student_Model.objects.get(id = id)
    give_marks = Grade_Model.objects.filter(student_model = std)
    
    total_grade_point = 0
    total_cradit = 0 
    
    for mark in give_marks:
        subject_credits = int(mark.subject_model.subject_credit)
        
        if mark.marks >= 40:
            if mark.marks >= 80:
                grade_point = 4.00
            elif mark.marks >= 70:
                grade_point = 3.50
            elif mark.marks >= 65:
                grade_point = 3.25
            elif mark.marks >= 60:
                grade_point = 3.00
            elif mark.marks >= 55:
                grade_point = 2.75
            elif mark.marks >= 50:
                grade_point = 2.50
            elif mark.marks >= 45:
                grade_point = 2.25
            elif mark.marks >= 40:
                grade_point = 2.00
                
            total_cradit += subject_credits
            total_grade_point += subject_credits * grade_point
            cgpa = total_grade_point / total_cradit
            round_cgpa = round(cgpa, 2)
                
    
    
    context = {
        'student': std,
        'result': give_marks,
        'total_cradit': total_cradit,
        'total_grade_point': total_grade_point,
        'round_cgpa': round_cgpa
    }
    return render(request, 'result.html', context)

