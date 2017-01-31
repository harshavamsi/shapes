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
	url(r'^events/$', views.events, name = 'events'),
	url(r'^contact/$', views.contact, name = 'contact'),
	url(r'^dancecontact/$', views.dancecontact, name = 'dancecontact'),
	url(r'^musiccontact/$', views.musiccontact, name = 'musiccontact'),
	url(r'^quizcontact/$', views.quizcontact, name = 'quizcontact'),
	url(r'^theatrecontact/$', views.theatrecontact, name = 'theatrecontact'),
	url(r'^acmcontact/$', views.acmcontact, name = 'acmcontact'),
	url(r'^ieeecontact/$', views.ieeecontact, name = 'ieeecontact'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
