from django.db import models
from django.core.urlresolvers import reverse
from django import forms


class RetroIssue (models.Model):
	title = models.CharField(max_length=255)
	details = models.TextField(null=True,blank=True)
	created =  models.DateTimeField(auto_now_add=True)
	reissued =  models.DateTimeField(auto_now=True)
	solved = models.BooleanField(default=False)
	votes = models.IntegerField(default=0)
	actions = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return u'%s' % self.title

	class Meta:
		#ordering = ["solved", "-votes"]
		ordering = ["-created", "-votes"]

class RetroIssueModelForm(forms.ModelForm):
	class Meta:
		model = RetroIssue
		fields = ["title","details"]
