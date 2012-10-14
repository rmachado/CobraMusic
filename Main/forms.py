from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label=u'Usuario')
    passwd = forms.PasswordInput(label=u'Email address')