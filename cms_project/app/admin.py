from django.contrib import admin
from app.models import Author, Category, Content
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Content)
admin.site.unregister(Group)