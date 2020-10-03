from django.shortcuts import render
from django.views import generic
from django.contrib.auth import login
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..models import User
from ..forms import TeacherSignUpForm
from ..decorators import teacher_required


class TeacherSignUpView(generic.CreateView):
    form_class = TeacherSignUpForm
    model = User
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('teacher_home'))


@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherHomeView(generic.TemplateView):
    template_name = 'classroom/teacher.html'
