from django.shortcuts import render
from home.models import Product
from django.contrib.postgres.search import SearchVector , SearchQuery , SearchRank , SearchHeadline, TrigramSimilarity
from django.db.models import Q

# Create your views here.
from django.shortcuts import render
from .models import Product
from django.contrib.postgres.search import (SearchVector, SearchQuery, SearchRank,
                                            TrigramSimilarity
                                            )
from django.db.models import Q
import time
from django.views.decorators.cache import cache_page

from django.core.cache import cache
# @cache_page(60 * 1)
def index(request):

    if search := request.GET.get('search'):
        query = SearchQuery(search)
        vector =  SearchVector(
            "title",
            "description",
            "category",
            "brand"
        )
        rank = SearchRank(vector, query)
        results = Product.objects.annotate(
            rank = rank,
            similarity = TrigramSimilarity('title', search) 
            + TrigramSimilarity('description', search) + TrigramSimilarity('category', search)
            + TrigramSimilarity('brand', search)
        ).filter(Q(rank__gte =0.3)| Q(similarity__gte = 0.3)).distinct().order_by('-rank', '-similarity')
    else:
        results = Product.objects.all()


    return render(request, 'index.html', {'results': results , 'search' : request.GET.get('search')})
