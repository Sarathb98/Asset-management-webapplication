from django.contrib import admin
from .models import  Register
from .models import Login
from .models import Asset

admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Asset)
