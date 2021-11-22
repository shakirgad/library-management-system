from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'rate_price_day',
            'rental_period',
            'total_rental',
            'status',
            'Category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_author':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'rate_price_day':forms.NumberInput(attrs={'class':'form-control','id':'rental_price'}),
            'rental_period':forms.NumberInput(attrs={'class':'form-control','id':'rental_day'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control','id':'rental_total'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'Category':forms.Select(attrs={'class':'form-control'}),
            
            }
class CatForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']