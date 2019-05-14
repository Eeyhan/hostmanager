from app01.models import Host
from rbac.forms.base import BaseForm


class HostModelForm(BaseForm):
    class Meta:
        model = Host
        fields = '__all__'
