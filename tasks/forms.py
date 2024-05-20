from django import forms
from .models import Word

class TranslationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        words = Word.objects.all()
        super().__init__(*args, **kwargs)
        for word in words:
            self.fields[f'translation_{word.id}'] = forms.CharField(label=word.russian, required=False)

