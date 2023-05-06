from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import Account

class AccountSiginupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountSiginupForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"]="form-control"

    class Meta:
        model = Account
        fields = ('username', 'password1', 'password2')


class AccountLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"]="form-control"
            
    class Meta:
        model = Account
        fields = ('username', 'password')

class AccountPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"]="form-control"
            
    class Meta:
        model = Account

class AccountAvatorUploadForm(ModelForm):
    class Meta:
        model = Account
        fields = ('avator',)