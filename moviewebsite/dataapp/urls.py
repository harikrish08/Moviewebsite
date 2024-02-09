from django.urls import path

from dataapp import views

app_name = 'dataapp'

urlpatterns = [
    path('add', views.add_movie, name='add_movie'),
    path('delete/<int:mov_id>', views.delete_movie, name='delete_movie'),
    path('update/<int:mov_id>', views.update_movie, name='update_movie'),
    path('movie/<int:movie_id>', views.add_review, name='add_review'),
    path('movie/<int:movie_id>/reviews', views.list_reviews, name='list_reviews'),
]
