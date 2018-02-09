from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='Your e-mail address')
    #email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)