from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clgbook.models import *
from clgbook.forms import *
from django.views.generic import TemplateView
from django.contrib.auth.views import *



def SignUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Your CollegeStack account has been create successfully.')
                form.save()
        else:
            form = RegistrationForm()
        return render(request, 'signup.html', {'form':form})
    else:
        return redirect('home')


def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = AuthenticationclassForm(request=request, data=request.POST)
            if forms.is_valid():
                em_us = forms.cleaned_data['username']
                pass_us = forms.cleaned_data['password']
                log = authenticate(email=em_us, password=pass_us)
                if log is not None:
                    login(request, log)
                    return redirect('home')
        else:
            forms = AuthenticationclassForm()
        return render(request, 'login.html', {'forms':forms})
    else:
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class HomeClass(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            colg_data = COllegeInformationModel.objects.filter(user=request.user)
            faculty_data = FacultiesModel.objects.filter(user=request.user)
            context = {'clg_data':colg_data, 'faculty_data':faculty_data}
            return render(request, 'clgbook/home.html', context)
        else:
            return redirect('login')


class FirstYearStudent(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        std_data = StudentsModel.objects.filter(user=request.user,student_course_year='First Year')
        std_bca_data = StudentsModel.objects.filter(user=request.user, student_course='BCA',student_course_year='First Year')
        std_b_tech_data = StudentsModel.objects.filter(user=request.user, student_course='B-Tech',student_course_year='First Year')
        std_hotel_Manage_data = StudentsModel.objects.filter(user=request.user, student_course='Hotel Management',student_course_year='First Year')
        std_mca_data = StudentsModel.objects.filter(user=request.user, student_course='MCA',student_course_year='First Year')
        std_m_tech_data = StudentsModel.objects.filter(user=request.user, student_course='M-Tech',student_course_year='First Year')
        std_b_com_data = StudentsModel.objects.filter(user=request.user, student_course='B-Com',student_course_year='First Year')
        context = {'clg_data':colg_data,'std_bca_data':std_bca_data,'std_b_tech_data':std_b_tech_data,
        'std_hotel_Manage_data':std_hotel_Manage_data,'std_mca_data':std_mca_data,'std_m_tech_data':std_m_tech_data,
        'std_b_com_data':std_b_com_data,'std_data':std_data}
        return render(request, 'clgbook/first_year.html', context)


class SecondYearStudent(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        std_data = StudentsModel.objects.filter(user=request.user,student_course_year='Second Year')
        std_bca_data = StudentsModel.objects.filter(user=request.user, student_course='BCA',student_course_year='Second Year')
        std_b_tech_data = StudentsModel.objects.filter(user=request.user, student_course='B-Tech',student_course_year='Second Year')
        std_hotel_Manage_data = StudentsModel.objects.filter(user=request.user, student_course='Hotel Management',student_course_year='Second Year')
        std_mca_data = StudentsModel.objects.filter(user=request.user, student_course='MCA',student_course_year='Second Year')
        std_m_tech_data = StudentsModel.objects.filter(user=request.user, student_course='M-Tech',student_course_year='Second Year')
        std_b_com_data = StudentsModel.objects.filter(user=request.user, student_course='B-Com',student_course_year='Second Year')
        context = {'clg_data':colg_data,'std_bca_data':std_bca_data,'std_b_tech_data':std_b_tech_data,
        'std_hotel_Manage_data':std_hotel_Manage_data,'std_mca_data':std_mca_data,'std_m_tech_data':std_m_tech_data,
        'std_b_com_data':std_b_com_data,'std_data':std_data}
        return render(request, 'clgbook/second_year.html', context)


class ThirdYearStudent(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        std_data = StudentsModel.objects.filter(user=request.user,student_course_year='Third Year')
        std_bca_data = StudentsModel.objects.filter(user=request.user, student_course='BCA',student_course_year='Third Year')
        std_b_tech_data = StudentsModel.objects.filter(user=request.user, student_course='B-Tech',student_course_year='Third Year')
        std_hotel_Manage_data = StudentsModel.objects.filter(user=request.user, student_course='Hotel Management',student_course_year='Third Year')
        std_mca_data = StudentsModel.objects.filter(user=request.user, student_course='MCA',student_course_year='Third Year')
        std_m_tech_data = StudentsModel.objects.filter(user=request.user, student_course='M-Tech',student_course_year='Third Year')
        std_b_com_data = StudentsModel.objects.filter(user=request.user, student_course='B-Com',student_course_year='Third Year')
        context = {'clg_data':colg_data,'std_bca_data':std_bca_data,'std_b_tech_data':std_b_tech_data,
        'std_hotel_Manage_data':std_hotel_Manage_data,'std_mca_data':std_mca_data,'std_m_tech_data':std_m_tech_data,
        'std_b_com_data':std_b_com_data,'std_data':std_data}
        return render(request, 'clgbook/third_year.html', context)


class FourthYearStudent(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        std_data = StudentsModel.objects.filter(user=request.user,student_course_year='Fourth Year')
        std_bca_data = StudentsModel.objects.filter(user=request.user, student_course='BCA',student_course_year='Fourth Year')
        std_b_tech_data = StudentsModel.objects.filter(user=request.user, student_course='B-Tech',student_course_year='Fourth Year')
        std_hotel_Manage_data = StudentsModel.objects.filter(user=request.user, student_course='Hotel Management',student_course_year='Fourth Year')
        std_mca_data = StudentsModel.objects.filter(user=request.user, student_course='MCA',student_course_year='Fourth Year')
        std_m_tech_data = StudentsModel.objects.filter(user=request.user, student_course='M-Tech',student_course_year='Fourth Year')
        std_b_com_data = StudentsModel.objects.filter(user=request.user, student_course='B-Com',student_course_year='Fourth Year')
        context = {'clg_data':colg_data,'std_bca_data':std_bca_data,'std_b_tech_data':std_b_tech_data,
        'std_hotel_Manage_data':std_hotel_Manage_data,'std_mca_data':std_mca_data,'std_m_tech_data':std_m_tech_data,
        'std_b_com_data':std_b_com_data,'std_data':std_data}
        return render(request, 'clgbook/fourth_year.html', context)


class StudentsEditClass(TemplateView):
    def get(self, request, student_name):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        std_data = StudentsModel.objects.filter(student_name=student_name)
        std_data2 = StudentsModel.objects.get(student_name=student_name)
        std_form = StudentFormClass(instance=std_data2)
        context = {'clg_data':colg_data, 'std_form':std_form, 'std_data':std_data}
        return render(request, 'clgbook/student_edit.html', context)

    def post(self, request, student_name):
        std_data = StudentsModel.objects.get(student_name=student_name)
        std_form = StudentFormClass(data=request.POST, files=request.FILES,instance=std_data)
        if std_form.is_valid():
            messages.success(request, 'Student data has been changed successfully.')
            std_form.save()
            return redirect('student_edit', std_data.student_name)


@login_required
def StudentDeleteView(request, student_name):
    std_1_data = StudentsModel.objects.filter(student_name=student_name,student_course_year='First Year')
    std_2_data = StudentsModel.objects.filter(student_name=student_name,student_course_year='Second Year')
    std_3_data = StudentsModel.objects.filter(student_name=student_name,student_course_year='Third Year')
    std_4_data = StudentsModel.objects.filter(student_name=student_name,student_course_year='Fourth Year')
    if std_1_data:
        if request.method == 'POST':
            std_1_data.delete()
            return redirect('first_year_data')
    elif std_2_data:
        if request.method == 'POST':
            std_2_data.delete()
            return redirect('second_year_data')
    elif std_3_data:
        if request.method == 'POST':
            std_3_data.delete()
            return redirect('third_year_data')
    elif std_4_data:
        if request.method == 'POST':
            std_4_data.delete()
            return redirect('fourth_year_data')


@method_decorator(login_required, name='dispatch') 
class SearchFirstYearStd(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        search_first_year_data = request.GET.get('search_first_year')
        std_data = StudentsModel.objects.filter(user=request.user,student_name__icontains=search_first_year_data,
        student_course_year='First Year')
        context = {'clg_data':colg_data,'std_data':std_data}
        return render(request, 'clgbook/search_first_year.html', context)    


@method_decorator(login_required, name='dispatch') 
class SearchSecondYearStd(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        search_second_year_data = request.GET.get('search_second_year')
        std_data = StudentsModel.objects.filter(user=request.user,student_name__icontains=search_second_year_data,
        student_course_year='Second Year')
        context = {'clg_data':colg_data,'std_data':std_data}
        return render(request, 'clgbook/search_second_year.html', context)   


@method_decorator(login_required, name='dispatch') 
class SearchThirdYearStd(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        search_third_year_data = request.GET.get('search_third_year')
        std_data = StudentsModel.objects.filter(user=request.user,student_name__icontains=search_third_year_data,
        student_course_year='Third Year')
        context = {'clg_data':colg_data,'std_data':std_data}
        return render(request, 'clgbook/search_third_year.html', context)    


@method_decorator(login_required, name='dispatch') 
class SearchFourthYearStd(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        search_fourth_year_data = request.GET.get('search_fourth_year')
        std_data = StudentsModel.objects.filter(user=request.user,student_name__icontains=search_fourth_year_data,
        student_course_year='Fourth Year')
        context = {'clg_data':colg_data,'std_data':std_data}
        return render(request, 'clgbook/search_fourth_year.html', context)    


@method_decorator(login_required, name='dispatch') 
class SearchFaculties(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        faculty_search = request.GET.get('faculties_search')
        faculty_data = FacultiesModel.objects.filter(user=request.user, faculty_name__icontains=faculty_search)
        context = {'clg_data':colg_data, 'faculty_data':faculty_data}
        return render(request, 'clgbook/search_faculties.html', context)    


@login_required
def Navbar(request):
    colg_data = COllegeInformationModel.objects.filter(user=request.user)
    context = {'clg_data':colg_data}
    return render(request, 'clgbook/navbar.html', context)


@method_decorator(login_required, name='dispatch')      
class TeachersClass(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        faculty_form = FacultiesFormClass()
        context = {'clg_data':colg_data, 'faculty_form':faculty_form}
        return render(request, 'clgbook/teacher.html', context)

    def post(self, request):
        faculty_form = FacultiesFormClass(data=request.POST, files=request.FILES)
        if faculty_form.is_valid():
            usr = request.user
            fim = faculty_form.cleaned_data['faculty_image']
            fnm = faculty_form.cleaned_data['faculty_name']
            fage = faculty_form.cleaned_data['faculty_age']
            fad = faculty_form.cleaned_data['faculty_add']
            fdiv = faculty_form.cleaned_data['faculty_teach_in_which_div']
            fcls = faculty_form.cleaned_data['faculty_teach_in_which_class']
            fyer = faculty_form.cleaned_data['faculty_teach_in_which_year']
            fgen = faculty_form.cleaned_data['gender']
            fsal = faculty_form.cleaned_data['salary']
            fjd = faculty_form.cleaned_data['joined_date']
            reg = FacultiesModel(user=usr,faculty_image=fim,faculty_name=fnm,faculty_age=fage,faculty_add=fad,
            faculty_teach_in_which_div=fdiv,faculty_teach_in_which_class=fcls,faculty_teach_in_which_year=fyer,
            gender=fgen,salary=fsal,joined_date=fjd)
            messages.success(request, 'Faculty data has been created successfully.')
            reg.save()
            return redirect('teachers')


@method_decorator(login_required, name='dispatch') 
class FacultyDataEdit(TemplateView):
    def get(self, request, faculty_name):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        faculty_data1 = FacultiesModel.objects.filter(faculty_name=faculty_name)
        faculty_data = FacultiesModel.objects.get(faculty_name=faculty_name)
        faculty_form = FacultiesFormClass(instance=faculty_data)
        context = {'clg_data':colg_data,'faculty_data':faculty_data1,'faculty_form':faculty_form}
        return render(request, 'clgbook/teacher_edits.html', context)

    def post(self, request, faculty_name):
        faculty_data = FacultiesModel.objects.get(faculty_name=faculty_name)
        faculty_form = FacultiesFormClass(data=request.POST,files=request.FILES, instance=faculty_data)
        if faculty_form.is_valid():
            messages.success(request, 'Faculty data has been changed successfully.')
            faculty_form.save()            
            return redirect('faculty_edits', faculty_data.faculty_name)


@login_required
def FacultyDelete(request, faculty_name):
    if request.method == 'POST':
        faculty_data = FacultiesModel.objects.get(faculty_name=faculty_name)
        faculty_data.delete()
        return redirect('home')


@method_decorator(login_required, name='dispatch')      
class StudentsClass(TemplateView):
    def get(self, request):
        std_form = StudentFormClass()
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        context = {'std_form':std_form,'clg_data':colg_data}
        return render(request, 'clgbook/student.html', context)

    def post(self, request):
        std_form = StudentFormClass(data=request.POST, files=request.FILES)
        if std_form.is_valid():
            usr = request.user
            si = std_form.cleaned_data['student_image']
            sn = std_form.cleaned_data['student_name']
            sr = std_form.cleaned_data['student_roll']
            sa = std_form.cleaned_data['student_age']
            sd = std_form.cleaned_data['student_div']
            sad = std_form.cleaned_data['student_add']
            sc = std_form.cleaned_data['student_course']
            scy = std_form.cleaned_data['student_course_year']
            sg = std_form.cleaned_data['gender']
            sf = std_form.cleaned_data['student_fees']
            sdat = std_form.cleaned_data['addmission_date']
            reg = StudentsModel(user=usr,student_image=si,student_name=sn,student_roll=sr,student_age=sa,student_div=sd,
            student_add=sad,student_course=sc, student_course_year=scy,gender=sg,addmission_date=sdat,student_fees=sf)
            messages.success(request, 'Student data has been created successfully.')
            reg.save()
            return redirect('students')


@method_decorator(login_required, name='dispatch')
class AccoutntsCLass(TemplateView):
    def get(self, request, username):
        user_data = CollegeAccount.objects.filter(username=username)
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        context = {'clg_data':colg_data}
        return render(request, 'clgbook/accounts.html', context)


@method_decorator(login_required, name='dispatch')
class CollegeInfoClass(TemplateView):
    def get(self, request):
        form = CollegeInformationForm()
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        context = {'form':form,'clg_data':colg_data}
        return render(request, 'clgbook/edit.html', context)

    def post(self, request):
        form = CollegeInformationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            usr = request.user
            img = form.cleaned_data['clg_image']
            uni_img = form.cleaned_data['clg_university_img']
            add = form.cleaned_data['college_address']
            pri = form.cleaned_data['college_priciple']
            hod = form.cleaned_data['college_HOD']
            uni = form.cleaned_data['college_university']
            reg = COllegeInformationModel(user=usr,clg_image=img,clg_university_img=uni_img,college_address=add,
            college_priciple=pri,college_HOD=hod,college_university=uni)
            reg.save()
            return redirect('edits_update', reg.pk)


@method_decorator(login_required, name='dispatch')
class CollegeInfoUpdate(TemplateView):
    def get(self, request, pk):
        college_info = COllegeInformationModel.objects.get(pk=pk)
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        form = CollegeInformationForm(instance=college_info)
        context = {'form':form,'clg_data':colg_data}
        return render(request, 'clgbook/edit.html', context)

    def post(self, request, pk):
        college_info = COllegeInformationModel.objects.get(pk=pk)
        form = CollegeInformationForm(data=request.POST, files=request.FILES, instance=college_info)
        if form.is_valid():
            form.save()
            return redirect('edit')


@login_required
def COllegeInfoDelete(request, pk):
    if request.method == 'POST':
        clg_data = COllegeInformationModel.objects.get(pk=pk)
        clg_data.delete()
        return redirect('edits')


class COllegeDeleteView(TemplateView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        context = {'clg_data':colg_data}
        return render(request, 'clgbook/delete_college.html', context)


def DeleteAccount(request, pk):
    if request.method == 'POST':
        college_account = CollegeAccount.objects.filter(pk=pk)
        college_account.delete()
        return redirect('login')


@method_decorator(login_required, name='dispatch')
class COllegePersonalInfo(TemplateView):
    def get(self, request):
        form = CollegePersonalInfoForm(instance=request.user)
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        context = {'form':form,'clg_data':colg_data}
        return render(request, 'clgbook/college_info.html',context)

    def post(self, request):
        form = CollegePersonalInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('college_info')


@method_decorator(login_required, name='dispatch')
class ChangePasswordClass(PasswordChangeView):
    def get(self, request):
        form = ChangePasswordForm(request.POST)
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        context = {'form':form,'clg_data':colg_data}
        return render(request, 'clgbook/change_password.html', context)


@method_decorator(login_required, name='dispatch')
class ChangePasswordDOneCLass(PasswordChangeDoneView):
    def get(self, request):
        colg_data = COllegeInformationModel.objects.filter(user=request.user)
        context = {'clg_data':colg_data}
        return render(request, 'clgbook/password_change_done.html', context)


@method_decorator(login_required, name='dispatch')
class LogOutClass(LogoutView):
    next_page = '/accounts/login/'