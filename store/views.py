from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category
# Create your views here.
def store(request, category_urls = None):
    
    categories = None
    products = None
    
    if category_urls != None:
        
        #get_object_or_404 it will bring in the categories if found, otherwise it will return 404 error
        categories = get_object_or_404(Category, url=category_urls)
        products = Product.objects.filter(category = categories, is_available = True)
        product_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count' : product_count}
    return render(request, 'store/store.html', context)

def product_detail(request, category_urls, product_url):
    
    try:
        single_product = Product.objects.get(category__url=category_urls, url=product_url)
    #     #single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        #single_product.update(name="Puma shoes")
        if single_product:
            print("Found")
        else:
            print("Not found")
    except Exception as e:
        raise e
    
    context = {
         'single_product': single_product,
         }
        
    return render(request, 'store/product_detail.html', context)
