from django.contrib import admin

from .models import Category, Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ['name'],
    }


admin.site.register(Category, admin.ModelAdmin)
