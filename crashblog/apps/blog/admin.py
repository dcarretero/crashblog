from django.contrib import admin
from .models import Post,Category,Comment,Tag

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentItemInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

    
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Tag,TagAdmin)
