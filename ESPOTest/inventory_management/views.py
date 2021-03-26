from django.shortcuts import render, redirect
from .models import Inventory

def home(request):
    context = {
        'all_items': Inventory.objects.all()
    }
    return render(request, "home.html", context)

def add_item(request):
    Inventory.objects.create(
        item_name = request.POST['item'], 
        quantity = request.POST['quantity'], 
        sell_price = request.POST['sell'], 
        buy_price = request.POST['buy'])
    return redirect('/')

def item_display(request, item_id):
    context = {
        'item' : Inventory.objects.get(id = item_id)
    }
    return render(request, 'item.html', context)

def delete_item(request, item_id):
    item = Inventory.objects.get(id = item_id)
    item.delete()
    return redirect('/')
# Feel free to make more views as needed