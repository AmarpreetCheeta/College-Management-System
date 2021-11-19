
from django.contrib import admin
from django.urls import path, include
from clgbook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clgbook.urls')),
    path('accounts/signup/', views.SignUp,name='signup'),
    path('accounts/login/', views.Login,name='login'),
]
