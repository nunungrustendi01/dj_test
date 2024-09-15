from django.contrib import admin
from .models import *
# Register your models here.

class TestModelAdmin(admin.ModelAdmin):
    models = TestModel


admin.site.register(TestModel, TestModelAdmin)