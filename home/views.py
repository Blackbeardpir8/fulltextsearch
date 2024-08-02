from django.shortcuts import render
from home.models import Product
from django.contrib.postgres.search import SearchVector , SearchQuery , SearchRank

# Create your views here.
def index(request):
    search = request.GET.get('search')
    if search:
        query = SearchQuery(search)
        vector = SearchVector('title' ,'category','brand','sku')
        rank = SearchRank(vector,query)
        results = Product.objects.annotate(
            rank = rank 
        ).filter(rank__gte=.06).order_by('-rank')
    else:
        results = Product.objects.all()

    for result in results:
        print(result.rank)
        

    return render(request, 'index.html', {'results': results , 'search' : request.GET.get('search')})
