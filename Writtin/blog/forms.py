from django import forms
from .models import Post


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={
                'class': 'form-control mb-3'
            }),
            'content': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }
