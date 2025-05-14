# myapp/urls.py
from django.shortcuts import render
from django.urls import path
from .views import MyLoginView, admin_login, maintenance_login, landing_page, dashboard, \
    issue_equipment, return_equipment, goods_list, issued_goods_list, student_logs_list, \
    goods_list, issued_goods_list, student_logs_list , AdminLoginView , MaintenanceLoginView

from django.contrib import admin
from django.urls import path, include
from .views import MyLoginView, admin_login, maintenance_login, landing_page, dashboard, \
    issue_equipment, return_equipment, goods_list, issued_goods_list, student_logs_list, AdminLoginView, MaintenanceLoginView

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin_login/', AdminLoginView.as_view(), name='admin_login_view'),
    path('maintenance_login/', MaintenanceLoginView.as_view(), name='maintenance_login'),

    # URLs for the buttons on the dashboard
    path('issue_equipment/', issue_equipment, name='issue_equipment'),
    path('return_equipment/', return_equipment, name='return_equipment'),
    path('view_available_goods/', goods_list, name='view_available_goods'),
    path('view_issued_goods/', issued_goods_list, name='view_issued_goods'),
    path('view_student_logs/', student_logs_list, name='view_student_logs'),

    # URLs for the goods (remove duplicated paths)
    path('goods/', goods_list, name='goods_list'),
    path('issued_goods/', issued_goods_list, name='issued_goods_list'),
    path('student_logs/', student_logs_list, name='student_logs_list'),

     path('error/', lambda request: render(request, 'error.html'), name='error'),
]