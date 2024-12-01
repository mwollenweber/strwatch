from sqlite3 import adapt

from django.contrib import admin
from strwatch.models import DataSource, Search

admin.site.register(Search)
admin.site.register(DataSource)
