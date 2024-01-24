from django.urls import path, re_path
from django.views.generic.base import RedirectView

from .views import PostCreate, PostsList, PostDetail, logoutuser, PostUpdate, ReactionCreate, ReactionList, PostDelete, \
    ReactionAccept, ReactionDelete


urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url='/admin'), name='redirect-admin'),
    path('logout', logoutuser, name='logout'),
    path('', PostsList.as_view(), name='posts'),
    path('posts/create/', PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post'),
    path('posts/<int:pk>/edit', PostUpdate.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('posts/<int:pk>/reactions', ReactionCreate.as_view(), name='reaction'),
    path('reactions/', ReactionList.as_view(), name='reactions'),
    path('reactions/accept/<int:pk>', ReactionAccept.as_view(), name='reactions_accept'),
    path('reactions/delete/<int:pk>', ReactionDelete.as_view(), name='reactions_delete'),

]
