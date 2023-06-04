from django import forms
from django.core import validators


def start_with_m(value):
    if value[0] != 'm':
        raise forms.ValidationError('Name should start with M')


class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[start_with_m])
    email = forms.EmailField(validators=[validators.MinLengthValidator(10)])
    # password = forms.IntegerField(min_value=5)
    # agree = forms.BooleanField(label_suffix=' ', label='I Agree')

    # def clean(self):
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    # if len(valname) < 4:
    #     raise forms.ValidationError('Enter more than or equal 4 character')

    # if len(valemail) < 10:
    #     raise forms.ValidationError(
    #         'Enter the correct email which is greater than 10 character s')
