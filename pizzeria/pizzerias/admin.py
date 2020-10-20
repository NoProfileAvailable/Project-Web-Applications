from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping


admin.site.register(Pizza)
# p_admin
# roottoor
admin.site.register(Topping)
