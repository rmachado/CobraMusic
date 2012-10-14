from dajaxice.utils import deserialize_form
from dajax.core import Dajax
import forms
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = forms.LoginForm(deserialize_form(form))

    if form.is_valid():
        dajax.remove_css_class('#my_form input', 'error')
        dajax.alert("Form is_valid(), your username is: %s" % form.cleaned_data.get('username'))
    else:
        dajax.remove_css_class('#my_form input', 'error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')

    return dajax.json()