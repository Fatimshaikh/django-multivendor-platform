from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    products = Product.objects.filter(user=request.user).exclude(user__isnull=True)
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

from django.contrib.auth.decorators import login_required

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  # don’t save yet
            product.user = request.user        # assign logged-in user
            product.save()                     # now save
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/create_product.html', {'form': form})
from django.contrib.auth import login
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = SignupForm()

    return render(request, 'products/signup.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)  # only owner can edit
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)  # only owner can delete
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/delete_product.html', {'product': product})