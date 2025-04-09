# forms.py
from django import forms
from .models import Contact
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control con-validate', 'id': 'contact-name', 'placeholder': 'نام'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control con-validate', 'id': 'contact-email', 'placeholder': 'ایمیل'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control con-validate', 'id': 'contact-message', 'placeholder': 'پیام شما'
            }),
        }
