from django import forms
from blog.models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
