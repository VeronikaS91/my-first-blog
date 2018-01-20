from django import forms
from .models import Post

class PostForm(forms.ModelForm): # formulář vytvořený z nějakého modelu
	class Meta:
		model = Post
		fields = ('title', 'text')