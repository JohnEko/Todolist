from django.conf.urls import url
from django.contrib import admin
from . import views
#from todo_list.views import todo_view
#from todo_list.views import about_view

urlpatterns = [
    url(r'^$', views.todo_view, name='Home'),
    url(r'^about_view/(?P<id>\d+)/$', views.about_view, name='about'),
    url(r'^update/', views.update, name='update'),
    url(r'^deleteTodo/(?P<id>\d+)/$', views.deleteTodo, name='delete'),
     #url(r'^deleteTodo/', views.deleteTodo, name='delete'),
    
]
