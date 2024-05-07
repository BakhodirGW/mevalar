from django.contrib import admin
from . models import *

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
admin.site.register(Notification, )
admin.site.register(Product)
admin.site.register(Category)