from django.contrib import admin
from django.utils.html import format_html
from .models import HomepageImage, BlogPost, Exhibition, Product, InfoPageContent

# -------------------------
# Homepage Content
# -------------------------

@admin.register(HomepageImage)
class HomepageImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image')

# -------------------------
# Info Page Content
# -------------------------

@admin.register(InfoPageContent)
class InfoPageContentAdmin(admin.ModelAdmin):
    list_display = ('bio', 'contact_email')
    fields = ('portrait', 'bio', 'contact_email')

# -------------------------
# Blog
# -------------------------

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'preview_image_tag')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('preview_image_tag',)
    exclude = ('created_at',)  # ✅ Prevent FieldError

    def preview_image_tag(self, obj):
        if obj.preview_image:
            return format_html('<img src="{}" width="150" />', obj.preview_image.url)
        return "-"
    preview_image_tag.short_description = 'Preview Image'

# -------------------------
# Exhibitions
# -------------------------

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date', 'location')
    list_filter = ('status', 'date')
    search_fields = ('title', 'description', 'location')

# -------------------------
# Shop / Products
# -------------------------

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('title', 'description')
