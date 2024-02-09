from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.shortcuts import render, get_object_or_404, redirect

from movieapp.models import Movies, Category, Review


def Allmoviecat(request, c_slug=None):
    c_page = None
    movie_list = None

    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        movie_list = Movies.objects.all().filter(category=c_page)
    else:
        movie_list = Movies.objects.all()
    paginator = Paginator(movie_list, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except (EmptyPage, InvalidPage):
        movies = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'category': c_page, 'movies': movies})


def Allmovie(request, c_slug, mov_slug):
    try:
        movie = Movies.objects.get(category__slug=c_slug, slug=mov_slug)
    except Exception as e:
        raise e
    return render(request, 'movie.html', {'movie': movie})


