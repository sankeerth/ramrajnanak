from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField()
	phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
	email = forms.EmailField(required = False)
	message = forms.CharField(widget=forms.Textarea, required = False)