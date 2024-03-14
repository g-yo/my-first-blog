from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views  # Importing Django's built-in login view


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<pk>/publish/',post_publish, name='post_publish'),
    path('post/<pk>/remove/',post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('drafts/',post_draft_list, name='post_draft_list'),
    path('post/new/',post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Define the login URL pattern
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Define the logout URL pattern




]
