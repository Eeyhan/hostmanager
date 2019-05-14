from django import forms
from app01.models import UserInfo
from django.core.exceptions import ValidationError
from rbac.forms.base import BaseForm


class UserModelForm(BaseForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'level', 'phone', 'depart', 'password', 'confirm_password', 'roles']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password


class UpdateUserModelForm(BaseForm):
    class Meta:
        model = UserInfo
        exclude = ['password']


class ResetUserModelForm(BaseForm):
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = UserInfo
        fields = ['password', 'confirm_password']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password
