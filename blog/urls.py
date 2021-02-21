from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("blogs/", views.BlogListView.as_view(), name="blogs"),
    path("blogs/<int:pk>", views.BlogDetailView.as_view(), name="blog-detail"),
    path("bloggers/", views.BlogAuthorListView.as_view(), name="bloggers"),
    path("bloggers/<int:pk>", views.BlogListbyAuthorView.as_view(), name="blogger-detail"),
    path("<int:pk>/create/", views.BlogCommentCreate.as_view(), name="create-comment"),
    path("comment/<int:pk>/delete/", views.BlogCommentDelete.as_view(), name="delete-comment"),
    path("blog/<int:pk>/update/", views.BlogUpdate.as_view(), name="update-blog"),
    path("blog/<int:pk>/delete/", views.BlogDelete.as_view(), name="delete-blog"),
    path("bloggers/<int:pk>/update/", views.BlogAuthorUpdate.as_view(), name="update-blogauthor"),
    path("profilpage/", views.ProfilPageListView.as_view(), name="profpage-user"),
    path("blog/newblogs/", views.SeeNewBlogsListView.as_view(), name="new-blogs"),
    path("blog/create/", views.BlogCreate.as_view(), name="create-blog"),
]