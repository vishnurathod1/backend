from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('student_home/', views.student_home, name='student_home'),
    path('js_trainer/', views.js_trainer, name='js_trainer'),
    path('css_trainer/', views.css_trainer, name='css_trainer'),
    path('java/', views.java_trainer, name='java'),
    path('python/', views.python_trainer, name='python'),
    path('subject_trainer/', views.subject_trainer, name='subject_trainer'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('registration/', views.registration, name='registration'),
    # Add more URL patterns for other pages as needed
]
