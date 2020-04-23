from django.contrib import admin
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
	list_display = ('title', 'type','status', 'created')
	list_filter = ('title','type', 'status')
	search_fields = ('title', )
	date_hierarchy = 'created'
	ordering = ['type', 'created']


admin.site.register(Banner, BannerAdmin)
