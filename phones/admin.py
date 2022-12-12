from django.contrib import admin

# Register your models here.
from phones.models import Phone

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Phone, PostAdmin)



