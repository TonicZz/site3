from django.contrib import admin
from main.models import *

class InstrumentAdmin(admin.ModelAdmin):
	list_display = ('name', 'tip')

class VideoAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')
	search_fields = ('name', 'category')
	list_filter = ('category','name',)
	#filter_horizontal = ('category','name',)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class TipaAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class TipInstrAdmin(admin.ModelAdmin):
	list_display = ('name', 'id')

admin.site.register(TipInstr, TipInstrAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Tipa, TipaAdmin)