from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course_description_page/', views.course_description_page, name='course_description_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('request_page/', views.request_page, name='request_page'),
    path('enrolled_courses_page/', views.enrolled_courses_page, name='enrolled_courses_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('dashboard/', views.dashboard_page, name='dashboard_page'),

    path('all_courses/', views.all_courses, name='all_courses'),
    path('student_info/', views.student_info, name='student_info'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('get_course_request/', views.get_course_request, name='get_course_request'),
    path('creat_course_request/', views.creat_course_request, name='creat_course_request'),
    path('get_course/', views.get_course, name='get_course'),
    path('learn/', views.learn_page, name='learn_page'),
    path('get_course_content/', views.get_course_content, name='get_course_content'),
    path('check_access/', views.check_access, name='check_access'),
    path('save_contact/', views.save_contact, name='save_contact'),
    path('get_quiz/', views.get_quiz, name='get_quiz'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('mark_lesson_complete/', views.mark_lesson_complete, name='mark_lesson_complete'),
    path('get_progress/', views.get_progress, name='get_progress'),
    path('get_certificate/', views.get_certificate, name='get_certificate'),
    path('get_dashboard/', views.get_dashboard, name='get_dashboard'),
]