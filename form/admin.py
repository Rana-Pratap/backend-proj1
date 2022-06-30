from django.contrib import admin
from form.models import Info



class InfoAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','uname','pinco']
# Register your models here.

admin.site.register(Info, InfoAdmin)

