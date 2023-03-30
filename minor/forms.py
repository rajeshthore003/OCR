from django import forms

class MyfileUploadForm(forms.Form):
    file_name = forms.forms.CharField( max_length=155)