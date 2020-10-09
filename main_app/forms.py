from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile

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
        fields = ('name','current_city', 'image')

class Image_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
