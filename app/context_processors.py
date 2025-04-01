from .forms import LoginForm


def global_forms(request):
    return {'login_form': LoginForm()}
