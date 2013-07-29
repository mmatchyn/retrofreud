from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token
#from django.utils.safestring import mark_safe
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from moodmeter.models import MoodProfile



def index(request):
	profiles = MoodProfile.objects.all()
	return render(request, 'moodmeter/index.html', {'profiles': profiles})

def vote(request, id):
	profile = 	get_object_or_404(MoodProfile,id=id)
	template = 'moodmeter/profile.html'

	if request.is_ajax():
		template = 'moodmeter/profile_ajax.html'

		mood = request.GET.get('mood')
		inc = int(request.GET.get('inc'))

		if mood == 'happy':
			new_value = profile.happiness + inc
			profile.happiness = new_value if new_value > 0 else 0
		elif mood == 'sad':
			new_value = profile.sadness + inc
			profile.sadness = new_value if new_value > 0 else 0
		elif mood == 'excited':
			new_value = profile.excitement + inc
			profile.excitement = new_value if new_value > 0 else 0
		elif mood == 'bored':
			new_value = profile.boredom + inc
			profile.boredom = new_value if new_value > 0 else 0
		elif mood == 'tired':
			new_value = profile.tiredness + inc
			profile.tiredness = new_value if new_value > 0 else 0

		profile.save()
	return render(request, template, {'profile':profile})

def vote_thumb(request, id):
	profile = 	get_object_or_404(MoodProfile,id=id)
	template = 'moodmeter/profile.html'

	if request.is_ajax():
		template = 'moodmeter/profile_thumb_ajax.html'

		inc = int(request.GET.get('inc'))

		if inc < 0:
			profile.thumbs_down -= inc #add positive :)
		else:
			profile.thumbs_up += inc

		profile.save()
	return render(request, template, {'profile':profile})

@requires_csrf_token
def update(request, id):
	profile = 	get_object_or_404(MoodProfile,id=id)
	c = {}
	c.update(csrf(request))
	template = "moodmeter/profile_suggestion_ajax.html"

	if request.method == 'POST':
		content = request.POST["activities"]
		profile.improvements = content
		profile.save()

	return render(request, template, {'profile':profile})


def profile(request, id, action='base'):
	profile = 	get_object_or_404(MoodProfile,id=id)

	template = 'moodmeter/profile.html'

	if request.is_ajax():
		#part = request.GET.get('part')
		part = action
		if  part == 'mood':
			template = "moodmeter/profile_ajax.html"
		elif part == 'thumbs':
			template = "moodmeter/profile_thumb_ajax.html"
		elif part == 'sug':
			template = "moodmeter/profile_suggestion_ajax.html"
	
	return render(request, template, {'profile':profile})
