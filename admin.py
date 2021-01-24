from django.contrib import admin
from Ecommerce.models import Formalshirt,Tshirt,Shirts

class FormalshirtAdmin(admin.ModelAdmin):
    list_display=('name','description','price','stock','available','created','updated')
class TshirtAdmin(admin.ModelAdmin):
    list_display=('name','description')
class ShirtsAdmin(admin.ModelAdmin):
    list_display=('name','description','price','stock','available','created','updated')
# Register your models here.
admin.site.register(Formalshirt,FormalshirtAdmin)
admin.site.register(Tshirt,TshirtAdmin)
admin.site.register(Shirts,ShirtsAdmin)



