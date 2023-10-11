from django import forms
from .models import Client, FundingProgram, Document

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class FundingProgramForm(forms.ModelForm):
    class Meta:
        model = FundingProgram
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all())

    class Meta:
        model = Document
        fields = ('client', 'uploaded_file')