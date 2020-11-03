from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Mixedmartialart, Entry
from .forms import MixedmartialartForm, EntryForm

def index(request):
	""" The home page for MMA. """
	return render(request, 'mma/index.html')

@login_required
def mixedmartialarts(request):
	""" Listing all Courses. """
	mixedmartialarts = Mixedmartialart.objects.filter(owner=request.user).order_by('date_added')
	context = {'mixedmartialarts': mixedmartialarts}
	return render(request, 'mma/mixedmartialarts.html', context)

@login_required
def course(request, course_id):
	""" Showing the entries form every course. """
	mixedmartialart = Mixedmartialart.objects.get(id=course_id)

	check_owner(request, mixedmartialart)
	# if mixedmartialart.owner != request.user:
	# 	raise Http404

	entries = mixedmartialart.entry_set.order_by('-date_added')
	context = {'mixedmartialart': mixedmartialart, 'entries': entries}
	return render(request, 'mma/course.html', context)

@login_required
def new_course(request):
	""" Adding new courses to the Site. """
	if request.method != 'POST':
		# No data submitted, create blank form
		form = MixedmartialartForm()
	else:
		form = MixedmartialartForm(data=request.POST)
		if form.is_valid():
			new_course = form.save(commit=False)
			new_course.owner = request.user
			new_course.save()
			# form.save()
			return redirect('mma:mixedmartialarts')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'mma/new_course.html', context)

@login_required
def new_entry(request, topic_id):
	""" Add a new entry for a particular topic. """
	course = Mixedmartialart.objects.get(id=topic_id)

	check_owner(request, course)
	# if course.owner != request.user:
	# 	raise Http404

	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = course
			new_entry.save()
			return redirect('mma:course', course_id=topic_id)

	# Display a blank or invalid form.
	context = {'course': course, 'form': form}
	return  render(request, 'mma/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	""" """
	entry = Entry.objects.get(id=entry_id)
	course = entry.topic

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('mma:course', course_id=course.id)

	context = {'entry': entry, 'course':course, 'form': form}
	return render(request, 'mma/edit_entry.html', context)


def check_owner(request, course):
	""" Checking which is logged in. """

	if course.owner != request.user:
		raise Http404












