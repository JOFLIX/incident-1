from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('create_ticket/',views.create_ticket,name='createticket'),
    path('agent_profile/',views.profile,name='agent_profile'),
    url(r'^search/$',views.search_results,name='search_results'),

]
