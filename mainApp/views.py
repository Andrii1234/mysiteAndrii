from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')


def  contact(request):
    return render(request, 'mainApp/basic.html', {'contact': ['если остальсь вопросы пишите нам',38003]})
