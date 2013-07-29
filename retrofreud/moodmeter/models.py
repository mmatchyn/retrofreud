from django.db import models
from django.core.urlresolvers import reverse

class MoodProfile(models.Model):
	title = models.CharField(max_length=255)
	created =  models.DateTimeField(auto_now_add=True)
	happiness = models.IntegerField(default=0)
	tiredness = models.IntegerField(default=0)
	sadness = models.IntegerField(default=0)
	boredom = models.IntegerField(default=0)
	excitement = models.IntegerField(default=0)

	thumbs_up = models.IntegerField(default=0, null="True")
	thumbs_down = models.IntegerField(default=0, null="True")
	improvements = models.TextField(null=True, blank="True")
	
	def __unicode__(self):
		return u'%s' % self.title

	class Meta:
		ordering = ["-created"]

	def getScores(self):
		positive = self.happiness + self.excitement
		neutral = self.boredom
		negative = self.tiredness + self.sadness

		score = {}
		score['positive'] = positive
		score['neutral'] = neutral
		score['negative'] = negative

		return score

	def get_max(self):
		return self.happiness + self.tiredness + self.sadness + self.boredom + self.excitement

	def get_positivity(self):
		return self.happiness + self.excitement

	def get_neutrality(self):
		return self.boredom

	def get_negativity(self):
		return self.tiredness + self.sadness