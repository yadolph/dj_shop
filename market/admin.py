from django.contrib import admin
from .models import Article, User, Product, Catalogue, Order
from django import forms
from ckeditor.widgets import CKEditorWidget


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

@admin.register(Catalogue)
class ProductAdmin(admin.ModelAdmin):
    pass
