from django import forms

from .models import Post, Aspirant, Test, Intresting

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'hierarchy')
        exclude = ['title', ...]

class AspirantForm(forms.ModelForm):

    class Meta:

        model = Aspirant
        fields = ('title', 'text', 'hierarchy', 'kurator', 'diser_name')

class TestForm(forms.ModelForm):

    class Meta:

        model = Test
        fields = ('title', 'text', 'hierarchy', 'kurator', 'diser_name')

class IntrestingForm(forms.ModelForm):

    class Meta:

        model = Intresting
        fields = ('title', 'text', 'hierarchy', 'kurator', 'diser_name')