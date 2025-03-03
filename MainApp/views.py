from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


author = {
    "Имя": "Евген",
    "Отчество" : "Борисович",
    "Фамилия": "Шершнев",
    "телефон": "8-923-666-03-66",
    "email": "Eugen@mail.ru"
    }

items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity" : 5},
   {"id": 2, "name": "Куртка кожаная", "quantity" : 2},
   {"id": 3, "name": "Coca-cola 1 литр", "quantity" : 12},
   {"id": 4, "name": "Картофель фри", "quantity" : 0},
   {"id": 5, "name": "Кепка", "quantity" : 124},
]


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

def get_item(request,item_id):
    for item in items:
        if item['id'] == item_id:
            res = f"""
            <h2>имя: {item["name"]} </h2>
            <p> количество: {item["quantity"]}</p>
            <p> <a href="/items"> Вернуться к списку товаров </a> </p>
            """
            return HttpResponse(res)
    return HttpResponseNotFound(f"Item with id={item_id} not found!")    

def get_items(request):
    res = "<h1>  список товаров </h1><ol>"
    for item in items:
        res += f""" <li><a href="/item/{item['id']}"> {item['name']} </li>"""
    res += "</ol>"
    return HttpResponse(res)    
