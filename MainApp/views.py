from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    context={
        'name': "дядя Евген",
        'email': 'Jeka@gmail.com'
    }

    return render(request,"index.html", context)

def about(request):
    author={
    "name": "Евген",
    "mid_name" : "Борисович",
    "last_name": "Шершнев",
    "phone": "8-923-666-03-66",
    "email": "Eugen@mail.ru"
    }
    
    return render(request,"about.html", {"author": author})

def get_item(request,item_id: int):
    try:
        item = Item.objects.get(id =item_id)
        colors = []
        # Check if element has at least one color
        if item.colors.exists():
            colors = item.colors.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found!")
    else:
        context = {"item": item,
                   "colors": colors,
                   }
        return render(request,"item_page.html", context)    
    


def get_items(request):
    items = Item.objects.all()
    context={"items": items} 
    return render(request,"items_list.html", context)