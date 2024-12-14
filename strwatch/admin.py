from sqlite3 import adapt

from django.contrib import admin
from strwatch.models import Search, STRrecord

admin.site.register(Search)
admin.site.register(STRrecord)
