from django.shortcuts import redirect, reverse, render
from django.views import generic


class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect(reverse('teacher_home'))
        elif request.user.is_student:
            return redirect(reverse('student_home'))

    return render(request, 'home.html')
