from django.urls import path

from . import views

app_name = 'userapp'

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('update/<int:id>/', views.updateprofile, name='updateprofile'),

]
