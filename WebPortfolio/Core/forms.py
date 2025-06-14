from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, min_length=3, max_length=20, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your name'
        }
    ))
    email = forms.EmailField(label='Correo', required=True, min_length=3, max_length=80, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your Mail'
        }
    ))
    phoneNumber = forms.CharField(label='Número', required=True, min_length=3, max_length=30, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Your phone number'
        }
    ))
    message = forms.CharField(label='Mensaje', required=True, min_length=10, max_length=300, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Massage',
            'rows':3
        }
    ))