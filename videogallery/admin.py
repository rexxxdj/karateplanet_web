from django.contrib import admin
from django.utils.html import format_html
from videogallery.models import Album, AlbumVideo
# Register your models here.

@admin.register(Album)
class AlbumModelAdmin(admin.ModelAdmin):
	def image_tag(self, obj):
		return format_html('<img src="{}" />'.format(obj.thumb.url))

	image_tag.short_description = 'Обложка'
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('image_tag','title','created','is_visible',)
	list_filter = ('created',)
	search_fields = ('title',)

@admin.register(AlbumVideo)
class AlbumVideoModelAdmin(admin.ModelAdmin):
    #def image_tag(self, obj):
    #    return format_html('<img src="{}" />'.format(obj.image_100.url))

    def album_title(self, obj):
    	return obj.album.title    

    album_title.short_description = 'Альбом'
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'album_title','video_normalize_url')
    list_filter = ('album', 'created')
    search_fields = ('title',)