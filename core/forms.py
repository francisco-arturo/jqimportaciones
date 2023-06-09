from django import forms
from .models import Category

class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
