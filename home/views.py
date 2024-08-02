from django.shortcuts import render
from home.models import Product

# Create your views here.
def index(request):
      
      results = Product.objects.all()
      
      return render(request, 'index.html',{'results':results})