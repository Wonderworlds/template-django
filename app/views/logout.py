from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


class Logout(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('index')
    login_url = reverse_lazy('index')

    def get_redirect_url(self, *args, **kwargs):
        try:
            logout(self.request)
            messages.success(self.request, "You have been logged out.")
        except Exception as e:
            messages.error(
                self.request, "An error occurred while logging out.")
            print(e)
        return super().get_redirect_url(*args, **kwargs)
