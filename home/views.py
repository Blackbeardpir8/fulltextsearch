from django.shortcuts import render
from home.models import Product

# Create your views here.
def index(request):
    search = request.GET.get('search')
    if search:
        results = Product.objects.filter(title__search=search)
    else:
        results = Product.objects.all()

    return render(request, 'index.html', {'results': results})
