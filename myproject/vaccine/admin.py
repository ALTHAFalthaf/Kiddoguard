from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=('fname','lname','email','phone','dob','role','password')
admin.site.register(User,UserAdmin)