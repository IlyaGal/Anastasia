from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^aspirant/$', views.aspirant_list, name='aspirant_list'),
    url(r'^aspirant/(?P<pk>\d+)/$', views.aspirant_detail, name='aspirant_detail'),
    url(r'^aspirant/new/$', views.aspirant_new, name='aspirant_new'),
    url(r'^aspirant/(?P<pk>\d+)/edit/$', views.aspirant_edit, name='aspirant_edit'),

    url(r'^test/$', views.test_list, name='test_list'),
    url(r'^test/(?P<pk>\d+)/$', views.test_detail, name='test_detail'),
    url(r'^test/new/$', views.test_new, name='test_new'),
    url(r'^test/(?P<pk>\d+)/edit/$', views.test_edit, name='test_edit'),

    url(r'^intresting/$', views.intresting_list, name='intresting_list'),
    url(r'^intresting/(?P<pk>\d+)/$', views.intresting_detail, name='intresting_detail'),
    url(r'^intresting/new/$', views.intresting_new, name='intresting_new'),
    url(r'^intresting/(?P<pk>\d+)/edit/$', views.intresting_edit, name='intresting_edit'),

    url(r'^testAnastasia/$', views.test_anastasia),
    url(r'^bookAnastasia/$', views.book_anastasia),
    url(r'^Aspirants/$', views.stat_aspirants),
    url(r'^AnastasiaKolorova/$', views.stat_anastasia),
    url(r'^AnastasiaKolorova1/$', views.stat_anastasia1),
    url(r'^page1/$', views.stat_page1),
    url(r'^page2/$', views.stat_page2),
    url(r'^page3/$', views.stat_page3),
    url(r'^page4/$', views.stat_page4),
    url(r'^page5/$', views.stat_page5),
    url(r'^Diagnostic/$', views.stat_diagnostic),
    url(r'^Info/$', views.stat_info),
    url(r'^Rozvutok/$', views.stat_rozvutok),

]