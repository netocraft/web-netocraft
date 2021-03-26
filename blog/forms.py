from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('texto', 'imagen')
        widgets = {
                    'texto': forms.Textarea(
                        attrs={'placeholder': 'Ingrese el contenido de su post aquí'}),
                }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = { k:"" for k in fields }

