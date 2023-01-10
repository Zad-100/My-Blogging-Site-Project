from django.contrib import admin

# Register your models here.

from .models import Headline, BlogContent

admin.site.register(Headline)
admin.site.register(BlogContent)