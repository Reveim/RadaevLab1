from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Excursion


User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class AddExcursionForm(forms.ModelForm):

    class Meta:
        model = Excursion
        fields = ['title', 'desc', 'time', 'pict']
        widgets = {
            'title': forms.TextInput(),
            'desc': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            'time': forms.TextInput(attrs={'type': 'time'})
        }
