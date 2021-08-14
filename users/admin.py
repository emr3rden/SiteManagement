from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Problems



class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name']

admin.site.register(CustomUser, CustomUserAdmin)





class ProblemAdmin(admin.ModelAdmin):

    list_display = ['author', 'problem', 'content', 'published_date']
    list_display_links = ['author', 'problem', 'content', 'published_date']
    list_filter = ['problem', 'published_date']

    class Meta:

        model = Problems

admin.site.register(Problems, ProblemAdmin)