#coding:utf-8
from django.contrib import admin
from test_admin.models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','update_time','pub_date')
    search_fields=['title']
admin.site.register(Article,ArticleAdmin)
