from django.urls import path

from movieapp import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.Allmoviecat, name='Allmoviecat'),
    path('<slug:c_slug>/', views.Allmoviecat, name='movie_cat'),
    path('<slug:c_slug>/<slug:mov_slug>', views.Allmovie, name='movie'),


]
