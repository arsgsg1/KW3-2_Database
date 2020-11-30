from django import forms
from .models import n_subject


class apply_form(forms.ModelForm):
    class Meta:
        model = n_subject
        fields = ['subject_id',]