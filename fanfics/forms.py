from django import forms
from .models import Publication, Comment
from taggit.forms import TagWidget

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'summary', 'content', 'tags')
        labels = {'title': 'Tytuł','summary': 'Opis', 'content': 'Treść', 'tags': 'Tagi'}
        widgets = {
            'tags': TagWidget(),
            'content': forms.Textarea(attrs={
                'cols': 200,
                'rows': 10,
                'style': 'width: 100%'
            }),
            'summary': forms.Textarea(attrs={
                'cols': 200,
                'rows': 5,
                'style': 'width: 100%'

            }),
            'title': forms.Textarea(attrs={
                'cols': 200,
                'rows': 2,
                'style': 'width: 100%'
            }),
            'tags': forms.Textarea(attrs={
                'cols': 200,
                'rows': 1,
                'style': 'width: 100%'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': ""}
        widgets = {
            'body' : forms.Textarea(attrs={
            'cols': 200,
            'rows': 10,
            'style': 'width: 100%'
        })}
