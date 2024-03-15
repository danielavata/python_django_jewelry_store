from multiprocessing.connection import Client

from django.contrib import admin

from products.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ContactRequest)
admin.site.register(Client)

