from django import forms
from .models import faculty,Student

class addFacultyForm(forms.ModelForm):
    class Meta:
        model=faculty
        fields="__all__"
        exclude={"password"}
        labels={"facultyid":"Enter Faculty Id"}

class addStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"password"}
        labels={"studentid":"Enter Student Id"}

