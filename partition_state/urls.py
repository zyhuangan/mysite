from django.conf.urls import url

from . import views

app_name='partition_state'
urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^show_check_partition',views.show_check_partition, name='show_check_partition'),
    url(r'^get_check_partition/(?P<project_name>[^\n]+)/$',views.get_check_partition, name='get_check_partition'),
	url(r'^show_newest_version_partition',views.show_newest_version_partition, name='show_newest_version_partition'),
    url(r'^get_newest_version_partition',views.get_newest_version_partition, name='get_newest_version_partition'),
	url(r'^show_detail_partition',views.show_detail_partition, name='show_detail_partition'),
	url(r'^GetProjectData/$',views.Return_Project_Data),
	url(r'^GetVersionData/$',views.Return_Version_Data),
    url(r'^get_detail_partition/(?P<platform_name>[0-9A-Z]+)/(?P<project_name>[^\n]+)/(?P<version_name>[^\n]+)/$',views.get_detail_partition, name='get_detail_partition'),
	url(r'^show_compare_partition',views.show_compare_partition, name='show_compare_partition'),
	#url(r'^get_compare_partition',views.get_compare_partition, name='get_compare_partition'),
	url(r'^compare_partition',views.compare_partition, name='compare_partition'),
	url(r'^detail_partition',views.detail_partition, name='detail_partition'),
	url(r'^check_partition/(?P<project_name>[0-9A-Z]+)/$',views.check_partition, name='check_partition'),
	url(r'^get_all_partition',views.get_all_partition, name='get_all_partition'),
]
