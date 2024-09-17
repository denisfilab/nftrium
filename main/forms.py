from django import forms
from main.models import NFT

class NFTForm(forms.ModelForm):
    class Meta:
        model = NFT
        fields = ['name', 'price', 'description', 'image', 'creator']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-indigo-500',
                'placeholder': 'Enter the name of the NFT'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-indigo-500',
                'placeholder': 'e.g., 0.5'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-indigo-500 h-32 resize-none',
                'placeholder': 'Provide a detailed description of your NFT'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 p-2.5 bg-white'
            }),
            'creator': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:border-indigo-500',
                'placeholder': "Enter the creator's name"
            }),
        }
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
