from django.contrib import admin
from webapp.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'detailed_description', 'status', 'created_at')
    list_filter = ('id', 'title', 'description', 'detailed_description', 'status', 'created_at')
    search_fields = ('title', 'description', 'detailed_description', 'status')
    fields = ('date', 'title', 'description', 'detailed_description', 'status', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Article, ArticleAdmin)
