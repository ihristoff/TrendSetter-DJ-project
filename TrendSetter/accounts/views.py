from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import forms as auth_forms

from django.urls import reverse_lazy, reverse

from TrendSetter.accounts.forms import AccountUserCreationForm
from TrendSetter.accounts.models import Profile

UserModel = get_user_model()

class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')

    #default will send it to accounts/profile so we override it
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class LogoutUserView(auth_views.LogoutView):
    template_name = 'accounts/logout-page.html'
    # we do not need 'success_url'  if we are using the 'next' approach in the form on the login-page
  #  success_url = reverse_lazy('index')


class RegisterUserView(views.CreateView):
    form_class = AccountUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    #code for auto login
    def form_valid(self, form):
        # form valid will call 'save'
        result = super().form_valid(form)
        login(self.request, form.instance)

        return result





class DetailsProfileView( views.DetailView):
    queryset = Profile.objects.prefetch_related().all()

    template_name = 'accounts/details-profile.html'


class UpdateProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    fields = ['trading_from', 'profile_image']
    template_name = 'accounts/update-profile.html'


    def get_success_url(self):
        return reverse('profile details', kwargs={'pk': self.object.pk})


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete-profile.html'