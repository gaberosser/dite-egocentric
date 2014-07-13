__author__ = 'gabriel'
from django.conf.urls import url
from traveltime import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.home, name='home'),
    url(r'^graph1/$', views.d3_sandbox, name='graph1'),
    url(r'^graph2/$', views.d3_sandbox2, name='graph2'),
    url(r'^async_pois/$', views.d3_async_pois, name='async_pois'),
    url(r'^create_data/$', views.create_data, name='create_data'),

    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]