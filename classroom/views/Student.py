from django.shortcuts import render
from django.views import generic
from django.contrib.auth import login
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..models import User
from ..forms import StudentSignUpForm
from ..decorators import student_required


class StudentSignUpView(generic.CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('student_home'))


@method_decorator([login_required, student_required], name='dispatch')
class StudentHomeView(generic.TemplateView):
    template_name = 'classroom/student.html'
