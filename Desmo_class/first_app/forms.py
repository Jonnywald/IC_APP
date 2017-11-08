from django import forms
from first_app.models import Users
from django.core import validators

class NewUser(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'

class TesteSimples(forms.Form):
    resp = forms.IntegerField()
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
