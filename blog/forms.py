from django import forms
from blog.models import Comment


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
