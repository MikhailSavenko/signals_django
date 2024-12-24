from django.contrib import admin
from .models import Review, User, Product, Notification


admin.site.register(Review)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Notification)