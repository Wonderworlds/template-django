from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from ..forms import SignUpForm
from django.contrib.auth import login


class SignUp(FormView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        if self.request.user.is_authenticated:
            messages.error(self.request, 'Already logged in!')
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: SignUpForm):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "SignUp OK.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "SignUp failed. Please try again.")
        return super().form_invalid(form)
