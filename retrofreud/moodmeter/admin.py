from django.contrib import admin
from moodmeter.models import MoodProfile


class MoodProfileAdmin(admin.ModelAdmin):
	list_display = ['title','happiness','tiredness','sadness','boredom','excitement']
	list_filter = ['created']
	search_fields = ['title']
	date_hierarchy = 'created'
	save_on_top = True
	

admin.site.register(MoodProfile, MoodProfileAdmin)