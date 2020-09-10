from django.shortcuts import render
from django.http import HttpResponse
from .models import food_list
from django.template import loader

# Create your views here.

# def index(request):
#    return HttpResponse("<h1>This is the food stock page")

def index(request):
    all_food = food_list.objects.all()
    # food_list.objects.create(name="hiiii", quantity="1111",unit="g",storage_type="fridge",category="fruit",expiry_date="2000-01-19")
    template = loader.get_template('food_stock/index.html')
    context = {
        'all_food': all_food
    }
    return HttpResponse(template.render(context, request))
