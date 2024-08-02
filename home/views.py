from django.shortcuts import render
from home.models import Product
from django.contrib.postgres.search import SearchVector

# Create your views here.
def index(request):
    search = request.GET.get('search')
    if search:
        results = Product.objects.annotate(
            search = SearchVector('title','category','description')
        ).filter(search = search)
    else:
        results = Product.objects.all()

    return render(request, 'index.html', {'results': results , 'search' : request.GET.get('search')})
