from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import User


class ManagerRequiredMixin(LoginRequiredMixin):
    """_Check if the user is a manager before granting access to the view_
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.user_type != 1:
            return self.handle_no_permission()
        return super(ManagerRequiredMixin, self).dispatch(request, *args, **kwargs)


class RegistrationView(ManagerRequiredMixin, CreateView):
    template_name = "authentication/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super(RegistrationView, self).form_valid(form)


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy("login")
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context
    

