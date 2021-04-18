from django import forms
from .models import Photos

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = [
            'answer1',
            'answer2',
            'answer3',
        ]