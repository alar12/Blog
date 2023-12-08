# blog/admin.py

from django.contrib import admin
from .models import UserProfile, BlogPost

admin.site.register(UserProfile)
admin.site.register(BlogPost)
