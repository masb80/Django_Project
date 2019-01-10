from django import forms

class formName(forms.Form):
    SSID = forms.CharField()
    Password = forms.CharField()
    #text = forms.CharField(widget=forms.Textarea)
    botchtcher = forms.CharField(required=False, widget=forms.HiddenInput)