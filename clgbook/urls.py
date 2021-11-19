from django.urls import path
from clgbook import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeClass.as_view(),name='home'),
    path('Faculties/', views.TeachersClass.as_view(),name='teachers'),
    path('students/', views.StudentsClass.as_view(),name='students'),

    path('edits/', views.CollegeInfoClass.as_view(),name='edits'),
    path('edits_update/<int:pk>/', views.CollegeInfoUpdate.as_view(),name='edits_update'),
    path('edits_delete/<int:pk>/', views.COllegeInfoDelete,name='edits_delete'),

    path('first_year_data/',views.FirstYearStudent.as_view(),name='first_year_data'),
    path('second_year_data/',views.SecondYearStudent.as_view(),name='second_year_data'),
    path('third_year_data/',views.ThirdYearStudent.as_view(),name='third_year_data'),
    path('fourth_year_data/',views.FourthYearStudent.as_view(),name='fourth_year_data'),

    path('search_result_first_year/',views.SearchFirstYearStd.as_view(),name='search_result_first_year'),
    path('search_result_second_year/',views.SearchSecondYearStd.as_view(),name='search_result_second_year'),
    path('search_result_third_year/',views.SearchThirdYearStd.as_view(),name='search_result_third_year'),
    path('search_result_fourth_year/',views.SearchFourthYearStd.as_view(),name='search_result_fourth_year'),

    path('search_faculties/',views.SearchFaculties.as_view(),name='search_faculties'),

    path('students_edit/<student_name>/',views.StudentsEditClass.as_view(),name='student_edit'),
    path('students_delete/<student_name>/',views.StudentDeleteView,name='student_delete'),

    path('faculty_edits/<faculty_name>/',views.FacultyDataEdit.as_view(),name='faculty_edits'),
    path('faculty_delete/<faculty_name>/',views.FacultyDelete,name='faculty_delete'),

    path('college_info/', views.COllegePersonalInfo.as_view(),name='college_info'),

    path('change_password/', views.ChangePasswordClass.as_view(success_url='/change_password_done/'),name='change_password'),
    path('change_password_done/', views.ChangePasswordDOneCLass.as_view(),name='change_password_done'),

    path('account/<username>/', views.AccoutntsCLass.as_view(),name='account'),

    path('account_delete/', views.COllegeDeleteView.as_view(),name='account_delete'),
    path('delete/<int:pk>/', views.DeleteAccount,name='delete'),

    path('logout/', views.LogOutClass.as_view(),name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)