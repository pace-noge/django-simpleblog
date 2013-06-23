from django.contrib import admin
from photo.models import Album, Image, Tag

class AlbumAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ["title"]

class TagAdmin(admin.ModelAdmin):
	list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
	#search_fields = ["title"]
	list_display = ["__unicode__", "title", "user", "rating", "size", "tags_", "albums_", "thumbnail","created"]
	list_filter = ["tags", "albums", "user"]

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

admin.site.register(Image, ImageAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)