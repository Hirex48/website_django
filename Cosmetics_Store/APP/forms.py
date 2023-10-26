from django import forms

class FormBuyProduct(forms.Form):
    name = forms.CharField(label='Имя', required=True)
    email = forms.EmailField(label='Электронная почта', required=False)
    phone_number = forms.CharField(label='Номер телефона', required=False)