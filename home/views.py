from django.shortcuts import render
from home.models import Product
from django.contrib.postgres.search import SearchVector , SearchQuery

# Create your views here.
def index(request):
    search = request.GET.get('search')
    if search:
        query = SearchQuery(search)
        results = Product.objects.annotate(
            search = SearchVector('title') + SearchVector('category') +  SearchVector('description')
        ).filter(search = query)
    else:
        results = Product.objects.all()

    return render(request, 'index.html', {'results': results , 'search' : request.GET.get('search')})
