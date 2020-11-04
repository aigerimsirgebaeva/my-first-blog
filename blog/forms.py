from django import forms

from .models import Post

class PostForm(forms.ModelForm): 

    class Meta:
        model = Post   #we tell Django which model should be used to create this form
        fields = ('title', 'text',)

#PostForm is the name of our form
# forms.ModelForm - We need to tell Django that this form is a ModelForm