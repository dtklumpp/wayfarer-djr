from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('users/<str:user_name>/edit/', views.edit_profile, name='edit_profile'),
    path('posts/<int:post_id>', views.post, name='post'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('semantic/', views.semantic, name='semantic'),
    path('carousel/', views.carousel_test, name='carousel'),
    path('users/<str:user_name>', views.profile, name='profile'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('users/default/<int:user_name>', views.profile, name='profile-login'),
    path('cities/<int:city_id>', views.city, name='city'),
    path('posts/create/<int:city_id>', views.create_post, name='create_post'),
    path('posts/edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('posts/delete/<int:post_id>/<int:city_id>', views.delete_post, name='delete_post'),
]
