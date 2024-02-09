from django import forms

from movieapp.models import Movies, Review


class addmovieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['title','desc','year','img','category','actors','rel_d','t_link']

class updatemovieform(forms.ModelForm):
    class Meta:
        model=Movies
        fields = ['title', 'desc', 'year', 'img', 'category', 'actors', 'rel_d', 't_link']



class Reviewform(forms.ModelForm):
    class Meta:
        model=Review
        fields=['review','rating']