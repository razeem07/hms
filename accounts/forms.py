from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=150,
        min_length=5,
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    password = forms.CharField(
        max_length=50,
        min_length=5,
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )

