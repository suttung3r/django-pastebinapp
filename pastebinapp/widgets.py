from django import forms
from django.utils.safestring import mark_safe

class CodeInputWidget(forms.widgets.Textarea):
    class Media:
        css = {
            'all': ('pastebinapp/CodeMirror/lib/codemirror.css'),
        }
        js = ('pastebinapp/CodeMirror/lib/codemirror.js', 
              'pastebinapp/CodeMirror/mode/clike/clike.js')
