# authentication/forms.py
from django import forms
from django.contrib.auth.models import User

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def clean_confirm_password(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Passwords don't match")
#         return confirm_password
