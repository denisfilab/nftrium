from django import forms
from main.models import NFT

class NFTForm(forms.ModelForm):
    class Meta:
        model = NFT
        fields = ['name', 'price', 'description', 'image', 'creator']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-300 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-indigo-500',
                'placeholder': 'Enter the name of the NFT'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-300 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-indigo-500',
                'placeholder': 'e.g., 0.5'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 text-gray-300 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-indigo-500 h-32 resize-none',
                'placeholder': 'Provide a detailed description of your NFT'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'border border-gray-600 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 p-2.5 bg-gray-800'
            }),
            'creator': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-300 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-indigo-500',
                'placeholder': "Enter the creator's name"
            }),
        }
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-300 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-indigo-500'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-300 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-indigo-500'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full px-3 py-2 text-gray-300 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-indigo-500'
            }),
        }