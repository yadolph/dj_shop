from django.contrib import admin
from .models import Article, User, Product, Catalogue, Order,TopCat
from django import forms
from ckeditor.widgets import CKEditorWidget
import json
from django.utils.html import format_html

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    brief = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'

class ArtcileAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    brief = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Article
        fields = '__all__'

class OrderAdminForm(forms.ModelForm):
    pretty_cart = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArtcileAdminForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

@admin.register(Catalogue)
class CatAdmin(admin.ModelAdmin):
    pass

@admin.register(TopCat)
class TopCatAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def pretty_cart_view(self,obj):
        return format_html(obj.pretty_cart)
    def user_email(self,obj):
        return obj.user.email
    pretty_cart_view.allow_tags = True
    readonly_fields = ('cart', 'pretty_cart', 'user')
    list_display = ['id', 'pretty_cart_view', 'completed','user_email']
    fields = ['cart', 'user', 'completed']



