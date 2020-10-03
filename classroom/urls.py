from django.urls import path

from .views import Teacher, Student

urlpatterns = [
    path('special/student/', Student.StudentHomeView.as_view(), name='student_home'),
    path('special/teacher/', Teacher.TeacherHomeView.as_view(), name="teacher_home"),
]