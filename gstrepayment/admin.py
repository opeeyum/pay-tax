from django.contrib import admin
from .models import Entry, OtherTaxes

# Register your models here.
admin.site.register(Entry)
admin.site.register(OtherTaxes)
