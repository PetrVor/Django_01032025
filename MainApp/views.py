from django.shortcuts import render
from django.http import HttpResponse


author = {
    "Имя": "Евген",
    "Отчество" : "Борисович",
    "Фамилия": "Шершнев",
    "телефон": "8-923-666-03-66",
    "email": "Eugen@mail.ru"
    }

def home(request):
    text =""" 
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Воробьев П.С.</i>
    """
    return HttpResponse(text)

def about(request):
    text=f"""
    "Имя": <b>{author['Имя']}</b><br>
    "Отчество" : "<b>{author['Отчество']}</b><br>
    "Фамилия": <b>{author['Фамилия']}</b><br>
    "телефон": <b>{author['телефон']}</b><br>
    "email": <b>{author['email']}</b><br>
    """

    return HttpResponse(text)