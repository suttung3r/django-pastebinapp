from django import forms
from django.db import models
from django.forms import ModelForm

from djchoices import DjangoChoices, ChoiceItem

from pastebinapp.widgets import CodeInputWidget

from compile_lang import SUPPORTED_LANGUAGES

# Create your models here.

class Snippet(models.Model):
    class LangType(DjangoChoices):
        C = ChoiceItem('C')
        CPP = ChoiceItem('C++')
        PYTHON = ChoiceItem('PYTHON')
        RUST = ChoiceItem('RUST')
    text = models.TextField(max_length=20000)
    lang = models.CharField(max_length=50,
                            choices=LangType.choices,
                            default=LangType.C)
    title = models.CharField(max_length=100,
                             default='None')

    def compile(self):
        return True

    def __str__(self):
        return '{}: {}'.format(self.title, self.text)

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['text', 'lang', 'title']
        widgets = {
            'text': CodeInputWidget()
        }
