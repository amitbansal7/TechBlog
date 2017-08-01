from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', post_list_view, name='post_list'),
    url(r'^login/$', user_login_view, name='user_login'),
    url(r'^logout/$', user_logout_view, name='user_logout'),
    url(r'^@(?P<username>\w+)/', profile_view, name='profile_view'),
    url(r'^post/$', post_list_view,),
    url(r'^post/draft$', post_draft_list_view, name='post_draft'),
    url(r'^post/tag/(?P<post_tag>\w+)/$', post_list_view_tag, name='post_tag'),
    url(r'^post/create$', post_create_view, name='post_create'),
    url(r'^post/(?P<pk>\d+)/$', post_detail_view, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/delete/', post_delete_view, name='post_delete'),
    url(r'^post/(?P<pk>\d+)/edit/', post_edit_view, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/rmdraft/', post_draft, name='post_draft'),
    url(r'^post/(?P<pk>\d+)/comment/', add_comment, name='add_comment'),
    url(r'^post/(?P<postpk>\d+)/comment-del/(?P<compk>\d+)/', delete_comment, name='delete_comment'),
]
