from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('users/<str:user_name>/edit/', views.edit_profile, name='edit_profile'),
    path('posts/<int:post_id>', views.post, name='post'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('semantic/', views.semantic, name='semantic'),
    path('carousel/', views.carousel_test, name='carousel'),
    path('users/<str:user_name>', views.profile, name='profile'),
    path('cities/<str:city_name>', views.city, name='city'),
    path('posts/create/<str:city_name>', views.create_post, name='create_post'),
    path('posts/edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('posts/delete/<int:post_id>/<int:city_id>', views.delete_post, name='delete_post'),
    
    # no view comments page, only edit
    # path('comments/<int:comment_id>', views.comment, name='comment'),
    path('comments/create/<int:post_id>', views.create_comment, name='create_comment'),
    path('comments/edit/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('comments/delete/<int:comment_id>', views.delete_comment, name='delete_comment'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
