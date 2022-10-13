from django.contrib import admin

from .models import Champion, Matches, SkinTheme

admin.site.register(Champion)
admin.site.register(Matches)
admin.site.register(SkinTheme)
