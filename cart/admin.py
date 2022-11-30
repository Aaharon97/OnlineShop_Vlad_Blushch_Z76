from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['price', 'amount', 'product']