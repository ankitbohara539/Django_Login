from django import forms
from .models import ProgrammingLanguage

class ProgrammingLanguageForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name', 'description', 'image', 'frameworks', 'founder']

   
    def clean_frameworks(self):
        frameworks = self.cleaned_data.get('frameworks')
        if len(frameworks) < 5:
            raise forms.ValidationError("Frameworks field should be at least 5 characters.")
        return frameworks
from django import forms


