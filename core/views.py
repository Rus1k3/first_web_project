from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        'title': 'Главная страница',
        'welcome_text': 'Добро пожаловать на OneMail!'
    }

    return render(request, 'ваше_приложение/index.html', context)


def about(request):
    return render(request, 'ваше_приложение/about.html')