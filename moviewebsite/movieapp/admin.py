from django.contrib import admin

from movieapp.models import Movies, Category, Review


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title','desc','year','category']
    list_editable = ['year','desc']
    prepopulated_fields = {'slug':('title',)}
    list_per_page = 20
admin.site.register(Movies,MoviesAdmin)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'review', 'rating','posted']
    list_editable = ['review', 'rating']
admin.site.register(Review,ReviewsAdmin)