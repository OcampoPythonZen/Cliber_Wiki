from django.contrib import admin

# Register your models here. I've set the super admin user such user:admin pass:admin
from .models import Post

admin.site.register(Post)
