from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('movieapp:movie_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Movies(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actors = models.TextField()
    desc = models.TextField()
    year = models.IntegerField()
    rel_d = models.DateField()
    t_link = models.URLField(max_length=500)
    added_by=models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='poster', default='null')

    class Meta:
        ordering = ('title',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def get_url(self):
        return reverse('movieapp:movie', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.title)

class Review(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.FloatField()
    status=models.BooleanField()
    posted = models.DateTimeField(auto_now_add=True)
