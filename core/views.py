from django.shortcuts import render, get_object_or_404
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


def email_detail(request, pk):

    email = get_object_or_404(
        EmailMessage,
        pk=pk
    )

    context = {
        'email': email
    }

    return render(
        request,
        'core/detail.html',
        context
    )
