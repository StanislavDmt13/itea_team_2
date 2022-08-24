from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from db.models import User, SocialPost

from django import forms

from django.forms.widgets import TextInput, PasswordInput


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            print("hello from __init")
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs=
                    {'class':'form-control',
                      'aria-label' : 'Username',
                      'aria-describedby' : 'basic-addon1'
            }),
            'email': TextInput(attrs=
                    {'class':'form-control',
                      'aria-label' : 'Username',
                      'aria-describedby' : 'basic-addon1'
            }),
        
        }


class CreatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(forms.ModelForm, self).__init__(*args, **kwargs)
            self.fields['post_title'].widget.attrs['class'] = 'form-control'
            self.fields['post_title'].widget.attrs['placeholder'] = 'Title'
            
            self.fields['post_photo'].widget.attrs['class'] = 'form-control  btn'
            self.fields['post_photo'].widget.attrs['placeholder'] = 'qwe1'
            
            self.fields['post_text'].widget.attrs['class'] = 'form-control'
            self.fields['post_text'].widget.attrs['placeholder'] = 'Post text'

            self.fields['post_is_private'].widget.attrs['placeholder'] = 'Confirm password'
            


    class Meta:
        model = SocialPost
        fields = ('post_title', 'post_photo', 'post_text', 'post_is_private')
        # widgets = {
        #     'username': TextInput(attrs=
        #             {'class':'form-control',
        #               'aria-label' : 'Username',
        #               'aria-describedby' : 'basic-addon1'
        #     }),
        #     'email': TextInput(attrs=
        #             {'class':'form-control',
        #               'aria-label' : 'Username',
        #               'aria-describedby' : 'basic-addon1'
        #     }),
        
        # }

        
            