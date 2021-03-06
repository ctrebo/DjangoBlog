from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r"^blogs/$", views.BlogListView.as_view(), name="blogs"),
    url(r"^blogs/(?P<pk>[0-9]+)$", views.BlogDetailView.as_view(), name="blog-detail"),
    url(r"^bloggers/$", views.BlogAuthorListView.as_view(), name="bloggers"),
    url(r"^bloggers/(?P<pk>[0-9]+)$", views.BlogListbyAuthorView.as_view(), name="blogger-detail"),
    url(r"^(?P<pk>[0-9]+)/create/$", views.BlogCommentCreate.as_view(), name="create-comment"),
    url(r"^comment/(?P<pk>[0-9]+)/delete/$", views.BlogCommentDelete.as_view(), name="delete-comment"),
    url(r"^blog/(?P<pk>[0-9]+)/update/$", views.BlogUpdate.as_view(), name="update-blog"),
    url(r"^blog/(?P<pk>[0-9]+)/delete/$", views.BlogDelete.as_view(), name="delete-blog"),
    url(r"^bloggers/(?P<pk>[0-9]+)/update/$", views.BlogAuthorUpdate.as_view(), name="update-blogauthor"),
    url(r"^profilpage/$", views.ProfilPageListView.as_view(), name="profpage-user"),
    url(r"^newblogs/$", views.SeeNewBlogsListView.as_view(), name="new-blogs"),
    url(r"^blog/create/$", views.BlogCreate.as_view(), name="create-blog"),
    url(r'^signup/$', views.signup, name='signup'),

]