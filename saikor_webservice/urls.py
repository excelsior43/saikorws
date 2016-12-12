from django.conf.urls import url
from saikor_webservice import views

urlpatterns = [
    url(r'^saikorians/$', views.SaikorianList.as_view()),
    url(r'^saikorians/(?P<pk>[0-9]+)/$', views.SaikorianDetail.as_view()),
   
]

