from django.contrib import admin
from django import forms
from .models import Book
from .widgets import AdminBookThumbnailWidget

class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'thumbnail' : AdminBookThumbnailWidget(),
        }

class BookAdmin(admin.ModelAdmin):
    """Book Administration"""
    form = BookAdminForm

prepopulated_fields = {"slug": ("title",)}

admin.site.register(Book, BookAdmin)
