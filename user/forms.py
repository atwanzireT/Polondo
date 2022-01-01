from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :', widget=forms.TextInput(
        attrs={'class': 'input'}))
    email = forms.EmailField(max_length=200,label= 'Email :', widget=forms.TextInput(
        attrs={'class': 'input'}))
    first_name = forms.CharField(max_length=100,label= 'First Name :', widget=forms.TextInput(
        attrs={'class': 'input'}))
    last_name = forms.CharField(max_length=100, label= 'First Name :', widget=forms.TextInput(
        attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )