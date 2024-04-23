from django.shortcuts import get_object_or_404, render
from .models import Product

# Create your views here.
def product_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def product_show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/show.html', {'product': product})
