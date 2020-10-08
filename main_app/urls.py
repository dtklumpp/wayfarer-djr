from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('users/<str:user_name>', views.profile, name='profile'),
    path('posts/<int:post_id>', views.post, name='post'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup'),
    path('semantic/', views.semantic, name='semantic'),
    
]
