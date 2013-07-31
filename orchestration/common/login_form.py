from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Rackspace SSO", 
    	widget=forms.TextInput(attrs={
    		'class': 'form-control', 
    		'placeholder':'Enter your Rackspace SSO'
    		}
    	))
    password = forms.CharField(label="Password", 
    	widget=forms.PasswordInput(attrs={
    		'class': 'form-control', 
    		'placeholder':'Enter your Password'
    		}
    	))
