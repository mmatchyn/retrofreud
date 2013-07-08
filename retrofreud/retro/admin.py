from django.contrib import admin
from retro.models import RetroIssue


class RetroIssueAdmin(admin.ModelAdmin):
	list_display = ['title', 'details']
	list_filter = ['created']
	search_fields = ['title']
	date_hierarchy = 'created'
	save_on_top = True
	

admin.site.register(RetroIssue, RetroIssueAdmin)