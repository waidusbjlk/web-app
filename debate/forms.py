from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddDebateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"


    class Meta:
        model = Debate
        fields = ['title', 'slug','image', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200')
        return title
    # title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),label="Заголовок")
    # is_published = forms.BooleanField(label="Заголовок", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(),label="Заголовок", empty_label="Категоря не выбрана")