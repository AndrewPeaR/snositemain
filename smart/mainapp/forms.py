from .models import Email
from django.forms import ModelForm, EmailInput, EmailField


class EmailForm(ModelForm):
    email = EmailField(label='', widget=EmailInput(attrs={'class':'emailinput', "placeholder": "Введите электронную почту"}))

    class Meta:
        model = Email
        fields = ['email',]
        # widgets = {
        #     "email": EmailInput(attrs = {
        #         "class": "emailinput",
        #         "placeholder": "Введите электронную почту",
        #     }),
        # }
