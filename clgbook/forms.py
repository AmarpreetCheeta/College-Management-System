from django.contrib.auth import forms
from django import forms
from clgbook.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='College Name',widget=forms.TextInput(
        attrs={'class':'_u7i89'}
    ))
    email = forms.CharField(label='College Email',widget=forms.EmailInput(
        attrs={'class':'_u7i89'}
    ))
    phone = forms.CharField(label='College Phone',widget=forms.NumberInput(
        attrs={'class':'_u7i89'}
    ))
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(
        attrs={'class':'_u7i89'}
    ))
    password2 = forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput(
        attrs={'class':'_u7i89'}
    ))
    class Meta:
        model = CollegeAccount
        fields = ['username','email','phone']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.pop('autofocus',None) 



class AuthenticationclassForm(AuthenticationForm):
    username = forms.CharField(label='College Email',widget=forms.EmailInput(
        attrs={'class':'_u7i89'}
    ))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(
        attrs={'class':'_u7i89'}
    ))



class CollegeInformationForm(forms.ModelForm):
    clg_image = forms.ImageField(label='College Image', widget=forms.FileInput(
        attrs={'class':'form-control mb-5'}
    ))
    clg_university_img = forms.ImageField(label='College University Image', widget=forms.FileInput(
        attrs={'class':'form-control'}
    ))
    college_address = forms.CharField(label='College Address', widget=forms.Textarea(
        attrs={'class':'form-control _ADDHJ','placeholder':'College Address'}
    ))
    college_priciple = forms.CharField(label='College Principle', widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'College Priciple'}
    ))
    college_HOD = forms.CharField(label='College HOD', widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'College HOD Name'}
    ))
    college_university = forms.CharField(label='College University', widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'College University Name'}
    ))   
    class Meta:
        model = COllegeInformationModel
        fields = ['clg_image','clg_university_img','college_address','college_priciple','college_HOD','college_university']


YEARS = [i for i in range(2015,2023)]

class StudentFormClass(forms.ModelForm):     
    class Meta:
        model = StudentsModel
        fields = ['student_image','student_name','student_roll','student_age','student_div','student_add',
            'student_course','student_course_year','gender','student_fees','addmission_date']

        widgets = {
            'student_div': forms.Select(attrs={'class':'form-select'}),
            'student_image' : forms.FileInput(attrs={'class':'form-control'}),
            'student_roll' : forms.NumberInput( attrs={'class':'form-control','placeholder':'Roll numbar'}),
            'student_age' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}),
            'student_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}),
            'student_add' : forms.Textarea(attrs={'class':'form-control _ADDHJ','placeholder':'Address'}),
            'student_course' : forms.Select(attrs={'class':'form-select'}),
            'student_course_year' : forms.Select(attrs={'class':'form-select'}),
            'gender' : forms.Select(attrs={'class':'form-select'}),
            'student_fees' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Student Fees'}),
            'addmission_date' : forms.SelectDateWidget(years=YEARS,attrs={'class':'_DTRE4'}),
        }


class FacultiesFormClass(forms.ModelForm):     
    class Meta:
        model = FacultiesModel
        fields = ['faculty_image','faculty_name','faculty_age','faculty_add','faculty_teach_in_which_div',
            'faculty_teach_in_which_class','faculty_teach_in_which_year','gender','salary','joined_date']

        widgets = {
            'faculty_image' : forms.FileInput(attrs={'class':'form-control'}),
            'faculty_name' : forms.TextInput( attrs={'class':'form-control','placeholder':'Faculty Name'}),
            'faculty_age' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}),
            'faculty_add' : forms.Textarea(attrs={'class':'form-control _ADDHJ','placeholder':'Faculty Address'}),
            'faculty_teach_in_which_div' : forms.Select(attrs={'class':'form-select'}),
            'faculty_teach_in_which_class' : forms.Select(attrs={'class':'form-select'}),
            'faculty_teach_in_which_year' : forms.Select(attrs={'class':'form-select'}),
            'gender' : forms.Select(attrs={'class':'form-select'}),
            'salary' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Faculty Salary'}),
            'joined_date' : forms.SelectDateWidget(years=YEARS,attrs={'class':'_DTRE4'}),
        }



class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='College Old Password', widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))
    new_password1 = forms.CharField(label='College New Password', widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))
    new_password2 = forms.CharField(label='College Confirm New Password', widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))


class CollegePersonalInfoForm(UserChangeForm):
    password = None
    username = forms.CharField(label='College Name',widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.CharField(label='College Email',widget=forms.EmailInput(
        attrs={'class':'form-control'}
    ))
    phone = forms.CharField(label='College Phone',widget=forms.NumberInput(
        attrs={'class':'form-control'}
    ))
    class Meta:
        model = CollegeAccount
        fields = ['username','email','phone']