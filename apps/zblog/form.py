from pagedown.widgets import AdminPagedownWidget
from django import forms

from .models import Entry


class EntryModelForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Entry
        fields = '__all__'
