""" Defines URL patterns for mma. """

from django.urls import path

from . import views

app_name = 'mma'

urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Page that shows all sports.
	path('courses/', views.mixedmartialarts, name='mixedmartialarts'),
	# Detail page for a single topic.
	path('courses/<int:course_id>', views.course, name='course'),
	# Page for adding new courses.
	path('new_course/', views.new_course, name='new_course'),
	# Page for adding a new entry.
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Pge for editing entries
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')

]