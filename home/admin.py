from django.contrib import admin
from .models import UserProfile,skills,eduction,photos
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(skills)
admin.site.register(eduction)
admin.site.register(photos)
