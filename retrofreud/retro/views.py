from django.core.context_processors import csrf
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from retro.models import RetroIssue, RetroIssueModelForm


#sam naredi validacijo
def add(request):
	template = 'retro/new_issue_dialog.html'
	form = RetroIssueModelForm()
	if request.method == 'POST':
		form = RetroIssueModelForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/issues/')
	ctx = {'form' : form}
	return render(request, template, ctx)


def index(request):

	inc_solved = False
	if request.method == 'GET':
		if request.GET.get('solved'):
			inc_solved = True

	if inc_solved:
		issues = RetroIssue.objects.all()
	else:
		issues = RetroIssue.objects.all().filter(solved=False)
	return render(request,'retro/index.html', {'issues': issues})

def sort(request, sort_column):

	template = 'retro/index_ajax.html'
	include_solved = False

	if request.GET.get('solved'):
		include_solved = bool(request.GET.get('solved'))

	if include_solved:
		issues = RetroIssue.objects.order_by(sort_column)
	else:
		issues = RetroIssue.objects.filter(solved=False).order_by(sort_column)

	#return redirect(request, 'index', {'issues': issues})
	return render(request, template, {'issues': issues})


# positive or negative profile, decide which emotions are in which profile
def issue(request, id):

	template = 'retro/issue.html'
	issue = get_object_or_404(RetroIssue,id=id)

	if request.is_ajax():
		template = 'retro/issue_ajax.html'

	return render(request, template, {'issue':issue})



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
	issue = get_object_or_404(RetroIssue,id=id)
	c = {}
	c.update(csrf(request))
	template = "retro/issue.html"

	if request.method == 'POST':
		content = request.POST["activities"]
		issue.actions = content
		issue.save()

	return render(request, template, {'issue':issue})

