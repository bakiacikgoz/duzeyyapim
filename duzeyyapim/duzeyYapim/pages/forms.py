from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': ''

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': ''

    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': ''

    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder': '',
        'style':'height:150px;',
    }))
    dept = forms.CharField(widget=forms.Select(attrs={
        'class':'form-select',
        'name':'dept',
    }))
    DEPARTMAN = (
        ('Belirtilmemiş', 'Seçiniz'),
        ('Ajans', 'Ajans'),
        ('Bilişim', 'Bilişim'),
        ('Tabela', 'Tabela'),
        ('Matbaa', 'Matbaa'),
        ('Prodüksiyon', 'Prodüksiyon'),
        ('Promosyon', 'Promosyon'),
        ('Dijital Baskı', 'Dijital Baskı'),
     )
    dept = forms.ChoiceField( widget=forms.Select(attrs={
        'class':'form-select',
        'name':'dept',
    }), choices=DEPARTMAN)
    class Meta:
        model = Contact
        fields = {'first_name','email','phone','message','dept'}