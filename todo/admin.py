from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    '''Admin View for Todo'''

    list_display = ('title', 'created_at', 'update_at', 'isCompleted', )