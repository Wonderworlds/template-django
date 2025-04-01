from django.contrib import messages
from django.contrib.auth import authenticate, login
from ..forms import LoginForm
from django.urls import reverse_lazy
from django.views.generic import RedirectView


class Login(RedirectView):
    url = reverse_lazy('index')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return self.get(request)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            print(form.errors)  # Debugging: Print form errors
        return self.get(request)
