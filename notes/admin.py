from django.contrib import admin

from .models import Author, Note


# Register the models so they appear in the Django admin area.
admin.site.register(Author)
admin.site.register(Note)
