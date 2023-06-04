from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'some'}))
    email = forms.EmailField()
    mobile = forms.IntegerField()
