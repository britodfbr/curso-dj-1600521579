from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Digite teu Nome'}))
    email = forms.EmailField(label='EMail', widget=forms.TextInput(attrs={'placeholder': 'Digite teu E-Mail'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Escreva tua mensagem'}))
