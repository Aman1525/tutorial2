from django.contrib import admin
from testApp.models import Hydjobs,Chennai,Pune,Bang

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class ChennaiAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

class PuneAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

class BangAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phonenumber']

admin.site.register(Hydjobs,HydjobsAdmin)
admin.site.register(Chennai,ChennaiAdmin)
admin.site.register(Pune,PuneAdmin)
admin.site.register(Bang,BangAdmin)

