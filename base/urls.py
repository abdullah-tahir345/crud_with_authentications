
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('add_student/', views.AddStudentPage, name='add_student'),
    path('delete_student/<int:std_id>/', views.DeleteStudent, name='delete_student'),
    path('update_student/<int:std_id>/', views.UpdateStudent, name='update_student'),
    path('do_update_student/<int:std_id>/', views.DoUpdateStudent, name='do_update_student'),
]