from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RegistrationForm



class RegistrationView(LoginRequiredMixin, CreateView):
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
    

