from django.conf.urls import patterns, include, url 
from django.contrib import admin 
from test_feature import views 
  
urlpatterns = patterns('', 
    # Examples: 
    # url(r'^$', 'MapPro.views.home', name='home'), 
    # url(r'^blog/', include('blog.urls')), 
  
    url(r'^map/$',views.Map), 
    url(r'^category_manage/$',views.category_manage),
    (r'^GetCityData/$',views.Return_City_Data), 
    (r'^GetCountryData/$',views.Return_Country_Data),
    url(r'^index/$',views.index), 
    url(r'^add/$',views.add),
    url(r'^$', views.index),
)
