from django.shortcuts import render
from .models import EmailMessage


def home(request):

    emails = EmailMessage.objects.all()

    context = {
        'title': 'Главная страница',
        'welcome_text': 'Добро пожаловать на OneMail!',
        'emails': emails
    }

    return render(request, 'core/index.html', context)


def about(request):
    return render(request, 'core/about.html')
