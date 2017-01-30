from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'studenthub'
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^clubs/cultural/$', views.culturalclubs, name = 'culturalclubs'),
	url(r'^clubs/technical/$', views.technicalclubs, name = 'technicalclubs'),
	url(r'^sports/$', views.sports, name = 'sports'),
	url(r'^activities/$', views.activities, name = 'activities'),
	url(r'^events/$', views.events, name = 'events'),
	url(r'^educationalsocieties/$', views.edusoc, name = 'edusoc'),
	url(r'^contact/$', views.contact, name = 'contact'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
