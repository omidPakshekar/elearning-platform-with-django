from django.urls import path
from . import views






app_name = 'students'
urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), name='student_register'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', views.StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<int:pk>/', views.StudenCourseDetailView.as_view(), name='student_course_detail'),
    path('course/<int:pk>/<int:module_id>/', views.StudenCourseDetailView.as_view(), name='student_course_detail_module'),

]
