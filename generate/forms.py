from django import forms
from .models import Brand,Model,Form1,Form2,Form3,Form4

class BookForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['model', 'brand', 'input_digi_port', 'input_ong_port','out_ong_port','digi_ong_port']
