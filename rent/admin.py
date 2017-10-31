from django.contrib import admin

from .models import Landlord,Rentneed,House,User


class LandlordAdmin(admin.ModelAdmin):
    fieldsets = [
        ("房东信息增加",
         {'fields':('llord_uid','llord_name','llord_nickname','llord_ID','llord_tel','llord_password')})
    ]

    list_display = ('id','llord_uid','llord_name','llord_nickname','llord_ID','llord_tel','llord_password','llord_create','llord_update')
    list_per_page = 50
    list_display_links = ('id','llord_uid','llord_name','llord_nickname','llord_ID','llord_tel')
    search_fields = ('id','llord_uid','llord_name','llord_nickname','llord_ID','llord_tel')
    date_hierarchy ='llord_create'

class RentneedAdmin(admin.ModelAdmin):
    fieldsets = [
        ("租房需求信息",{"fields":('rent_name','rent_addr','scope','rental','area','number','story','rent_type')})
    ]
    list_display = ('id','rent_name','rent_addr','scope','rental','area','number','story','rent_type','rent_create','rent_update')
    list_per_page = 50
    list_display_links = ('id','rent_name','rent_addr','scope','rental','area','number','story','rent_type','rent_create','rent_update')
    search_fields = ('id','rent_name','rent_addr','scope','rental','area','number','story','rent_type','rent_create','rent_update')
    date_hierarchy = 'rent_create'

class HouseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("房屋信息",{"fields":('house_name','address','community_name','house_type','house_tel','llord','is_rent','desc')})
    ]
    list_display = ('id','house_name','address','community_name','house_type','house_tel','llord','is_rent','desc','house_create','house_update')
    list_per_page = 50
    list_display_links = ('id','house_name','address','community_name','house_type','house_tel','llord','is_rent','desc')
    search_fields = ('id','house_name','address','community_name','house_type','house_tel','llord','is_rent','desc')
    date_hierarchy = 'house_create'

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("用户信息",
         {"fields": ('username', 'nickname', 'userid', 'birth', 'sex', 'tel', 'uid')})
    ]
    list_display = ('id','uid','username', 'nickname', 'userid', 'birth', 'sex', 'tel','user_create','user_update')
    list_per_page = 50
    list_display_links = ('id','username', 'nickname', 'userid', 'birth', 'sex', 'tel', 'uid')
    search_fields = ('id','username', 'nickname', 'userid', 'birth', 'sex', 'tel', 'uid')
    date_hierarchy = 'user_create'



admin.site.site_header = "租房分析管理平台"
admin.site.register(Landlord, LandlordAdmin)
admin.site.register(Rentneed, RentneedAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(User, UserAdmin)

