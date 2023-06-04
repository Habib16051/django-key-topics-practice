from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    r_password = forms.CharField(
        label="Password(again)", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpassword = cleaned_data['password']
        valrpassword = cleaned_data['r_password']

        if valpassword != valrpassword:
            raise forms.ValidationError('Password does not matched!')
