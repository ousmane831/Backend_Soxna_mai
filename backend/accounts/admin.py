from django.contrib import admin

from .models import User

# Register your models here.
admin.site.register(User)  # Assuming you have a User model in accounts/models.py