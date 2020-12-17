from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.views.generic import ListView, DetailView

# Create your views here.

class IndexView(ListView):
    template_name = 'app/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()

class ItemDetailView(DetailView):
    model = Item
    template_name = 'app/item-detail.html'

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ItemForm()

    return render(request,'app/create.html',{'form': form})

def edit(request, pk, template_name='app/edit.html'):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='app/confirm_delete.html'):
    item = get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('index')
    return render(request, template_name, {'object':item})