from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import Signupform, EditProfileForm
from blog.models import profile

# Create your views here.

class ShowProfilePageView(DetailView):
    model = profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        users = profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class UserRegisterView(generic.CreateView):
    form_class = Signupform
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
    
