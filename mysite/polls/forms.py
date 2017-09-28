#2017-09 Add posting board
from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
#2017-09 Add posting board
