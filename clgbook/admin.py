from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from clgbook.models import *


class CollageAccountAdmin(UserAdmin):
    list_display = ['id','username','email','phone','date_joined','last_login','is_admin','is_staff','is_active']
    search_fields = ['id','username','email','phone']
    readonly_fields = ['date_joined','last_login']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(CollegeAccount, CollageAccountAdmin)


class CollegeInformationAdmin(admin.ModelAdmin):
    list_display = ['user','clg_image','clg_university_img','college_address','college_priciple','college_HOD',
    'college_university','date_upload']
admin.site.register(COllegeInformationModel, CollegeInformationAdmin)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['user','student_image','student_name','student_roll','student_age','student_div','student_add',
        'student_course','student_course_year','gender','student_fees','addmission_date']
admin.site.register(StudentsModel, StudentsAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['user','faculty_image','faculty_name','faculty_age','faculty_add','faculty_teach_in_which_div',
    'faculty_teach_in_which_class','faculty_teach_in_which_year','gender','salary','joined_date']
admin.site.register(FacultiesModel, FacultyAdmin)