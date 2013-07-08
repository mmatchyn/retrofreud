from django.core.context_processors import csrf
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import requires_csrf_token
from retro.models import RetroIssue


def index(request):
	issues = RetroIssue.objects.all()
	return render(request,'retro/index.html', {'issues': issues})

# positive or negative profile, decide which emotions are in which profile
def issue(request, id):
	issue = get_object_or_404(RetroIssue,id=id)
	return render(request, 'retro/issue.html', {'issue':issue})


def vote(request, id):

	inc = int(request.GET.get('inc'))
	issue = get_object_or_404(RetroIssue,id=id)
	new_value = issue.votes + inc
	issue.votes = new_value if new_value > 0 else 0
	issue.save()

	issues = RetroIssue.objects.filter()
	return render(request, 'retro/index.html', {'issues':issues})



def close(request, id):

	issue = get_object_or_404(RetroIssue,id=id)
	issue.solved = True
	issue.save()

	issue = get_object_or_404(RetroIssue,id=id)
	return render(request, 'retro/issue.html', {'issue':issue})


def reopen(request, id):

	issue = get_object_or_404(RetroIssue,id=id)

	issue.solved = False
	issue.save()

	issue = get_object_or_404(RetroIssue,id=id)
	return render(request, 'retro/issue.html', {'issue':issue})


@requires_csrf_token
def update(request, id):
	issue = 	get_object_or_404(RetroIssue,id=id)
	c = {}
	c.update(csrf(request))
	template = "retro/issue.html"

	if request.method == 'POST':
		content = request.POST["activities"]
		issue.actions = content
		issue.save()

	return render(request, template, {'issue':issue})