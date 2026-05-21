from django import forms
from .models import EmailMessage

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Тема сообщения'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш email'
        })
    )

    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше сообщение',
            'rows': 5
        })
    )


class EmailMessageForm(forms.ModelForm):
    class Meta:
        model = EmailMessage

        fields = [
            'sender',
            'recipient',
            'subject',
            'message',
            'image',
            'tags'
        ]

        widgets = {
            'sender': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'recipient': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'subject': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control'
            })
        }
