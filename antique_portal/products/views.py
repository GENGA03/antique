from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        products = Product.objects.exclude(seller=request.user)
    else:
        products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})
# @login_required
# def post_product(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         starting_price = request.POST.get('starting_price')
#         image = request.FILES.get('image')
#         product = Product(title=title, description=description, starting_price=starting_price, image=image, seller=request.user)
#         product.save()
#         return redirect('home')
#     return render(request, 'products/post_product.html')

@login_required
def post_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        
        description = request.POST.get('description')
        starting_price = request.POST.get('starting_price')
        image = request.FILES.get('image')
        
       
        product = Product(title=title, description=description, starting_price=starting_price, image=image, seller=request.user)
        

        product.save()
        
       
        return redirect('home')
  
    return render(request, 'products/post_product.html')
