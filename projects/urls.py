from django.conf.urls import patterns, url

from projects import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.projects, name='projects'),
    )