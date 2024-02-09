from django.shortcuts import render

from movieapp.models import Movies, Category
from django.db.models import Q


# Create your views here.
def search(request):
    movies=None
    categories=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=Movies.objects.all().filter(Q(title__contains=query) | Q(desc__contains=query))
        categories=Category.objects.all().filter(Q(name__contains=query))
        return render(request,'search.html',{'query':query,'movies':movies,'categories':categories})