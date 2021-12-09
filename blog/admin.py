from django.contrib import admin
from .models import Category,Post
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','add_date')
    search_fields = ('title',)

class postAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =('title',)
    list_filter = ('cat',)
admin.site.register(Category,categoryAdmin)
admin.site.register(Post,postAdmin)
