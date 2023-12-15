from django import forms

class UserForm(forms.Form):
    name = forms.CharField(required=True, label='Имя', help_text='Help me')
    age = forms.IntegerField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'fsdfsdfsd'}))
    required_css_class = "myclass"

class UserForm2(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)