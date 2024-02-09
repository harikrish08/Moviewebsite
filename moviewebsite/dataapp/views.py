from django.shortcuts import render, redirect, get_object_or_404

from dataapp.form import addmovieform, updatemovieform, Reviewform

from django.utils.text import slugify

from movieapp.models import Movies, Review


# Create your views here.
def add_movie(request):
    if request.method == 'POST':
        form = addmovieform(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.slug = generate_slug(movie.title)
            movie.save()
            return redirect('/movie')
    else:
        form = addmovieform()
    return render(request, 'add.html', {'form': form})


def generate_slug(title):
    return slugify(title)


def delete_movie(request, mov_id):
    movie = get_object_or_404(Movies, pk=mov_id)

    if request.method == 'POST':
        if request.user == movie.added_by:
            movie.delete()
            return redirect('/movie')
        else:
            return render(request, 'error.html', {'message': 'You are not authorized to delete'})


def update_movie(request, mov_id):
    movie = Movies.objects.get(id=mov_id)
    form = updatemovieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        if request.user == movie.added_by:
            form.save()
            return redirect('/movie')
        else:
            return render(request, 'error.html', {'message2': 'You are not authorized to edit'})

    return render(request, 'update.html', {'form': form, 'movie': movie})


def add_review(request, movie_id):
    if request.method == 'POST':
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')
        movie = Movies.objects.get(id=movie_id)
        user = request.user

        review = Review.objects.create(
            movie=movie,
            user=user,
            review=review_text,
            rating=rating,
            status=True,
        )

        return redirect('/movie', movie_id=movie_id,review=review)
    return render(request, 'movie.html')




def list_reviews(request,movie_id):
    reviews = Review.objects.all().filter(movie_id=movie_id,status=True)
    return render(request, 'review.html', {'reviews': reviews})
