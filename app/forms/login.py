from django.contrib.auth.forms import UsernameField
from django import forms
from django.utils.translation import gettext as _


class LoginForm(forms.Form):
    username = UsernameField(
        required=True,
        min_length=4,
        max_length=32,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control',
                   'placeholder': _('username')}
        ),
        label=''
    )
    password = forms.CharField(
        required=True,
        strip=False,
        min_length=8,
        max_length=32,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                   'class': 'form-control',
                   'placeholder': _('password')}
        ),
        label=''

    )
