from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password','degree_good','trade_count', 'good_mark', 'bad_mark']
    #添加链接
    list_display_links = ['username']
    #添加可编辑字段
    #list_editable = ['address', 'city']
    #添加搜索框
    search_fields = ['username']
    #date_hierarchy = DateField
    #右面添加过滤器
    list_filter = ['username']

admin.site.register(User, UserAdmin)

class AdmirelogAdmin(admin.ModelAdmin):
    list_display = ['uid','fid','aid','isGood','isFile']
    list_display_links = ['uid']
# uid　fid　　aid　isGood　　isFile

admin.site.register(Admirelog, AdmirelogAdmin)


class CollegetypeAdmin(admin.ModelAdmin):
    list_display = ['title','desc']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['title']
admin.site.register(Collegetype, CollegetypeAdmin)

class CollegesAdmin(admin.ModelAdmin):
    list_display = ['title','desc']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['title']
admin.site.register(Colleges, CollegesAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['aim_user','have_read','arg0','arg1']
    list_display_links = ['aim_user']
admin.site.register(Notification, NotificationAdmin)