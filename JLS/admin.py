from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'image', 'description')
class MemberAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'password')
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')
  search_fields=['name','category__name']
admin.site.register(Catagory,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Member,MemberAdmin)
class cardAdmin(admin.ModelAdmin):
  list_display = ('user','product')
admin.site.register(Cart,cardAdmin)