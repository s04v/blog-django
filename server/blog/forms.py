from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post


# Create your forms here.

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text')