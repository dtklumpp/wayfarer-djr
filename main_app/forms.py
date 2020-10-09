from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile, Post

class User_Form(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ('user',)

class Profile_Edit_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ('name','current_city','image')

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

