from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

def product_edit(request, pk=None):
    instance = get_object_or_404(Product, pk=pk) if pk else None
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=instance)
    return render(request, 'product_form.html', {'form': form})