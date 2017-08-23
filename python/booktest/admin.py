from django.contrib import admin
from booktest.models import BookInfo, HeroInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'book_author', 'book_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'comment']

# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
