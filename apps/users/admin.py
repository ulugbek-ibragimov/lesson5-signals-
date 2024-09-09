from django.contrib import admin
from apps.users.models import User, UserProfile


#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass