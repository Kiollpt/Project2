from django.conf.urls import url
from django.contrib.auth.views import login,logout


from . import views

app_name = 'polls'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #2017.9.19 Add posting board#
    url(r'^(?P<question_id>[0-9]+)/post/$', views.post, name='post'),
    #2017.9.19 Add posting board#
    #2017.10.1 Add login/out mechanisim
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    #2017.10.1 Add login/out mechanisim


]
