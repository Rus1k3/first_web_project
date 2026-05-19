from django.shortcuts import render, get_object_or_404
from .models import EmailMessage
from .forms import FeedbackForm
from django.shortcuts import redirect


def home(request):
    emails = EmailMessage.objects.all()

    return render(request, 'core/index.html', {
        'title': 'Главная страница',
        'welcome_text': 'Добро пожаловать на OneMail!',
        'emails': emails
    })


def about(request):
    return render(request, 'core/about.html')


def email_detail(request, pk):
    email = get_object_or_404(EmailMessage, pk=pk)

    return render(request, 'core/detail.html', {
        'email': email
    })

def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')

    else:
        form = FeedbackForm()

    return render(request, 'core/contact.html', {
        'form': form
    })

