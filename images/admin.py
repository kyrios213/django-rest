from django.contrib import admin
from .models import Images, Category

class ImagesAdmin(admin.ModelAdmin):
    model = Images
    list_display = (
        'title', 'slug', 'author', 'created', 'status'
    )
    prepopulated_fields = {
        'slug': ('title',),
    }



admin.site.register(Images, ImagesAdmin)
admin.site.register(Category)
