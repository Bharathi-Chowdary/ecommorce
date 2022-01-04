from django.shortcuts import HttpResponse, render
from store.models import Product

def home(request):
    #instead of httpresponse, render is used to render all the templates
    #return HttpResponse("Homepage")
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products' : products
        }
    return render(request, 'home.html', context)