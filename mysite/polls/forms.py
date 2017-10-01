from django import forms
from .models import Comment
from django.contrib.auth.models import User

#2017.9.19 Add posting board
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
#2017.9.19 Add posting board

#2017.10.1 Add login mechanisim ?
class LoginForm(forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(widget=forms.PasswordInput)
#2017.10.1 Add login mechanisim ?
