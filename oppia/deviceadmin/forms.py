from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div
from gcm.forms import RegisterDeviceForm
from django import forms
from oppia.deviceadmin.models import UserDevice


class RegisterUserDeviceForm(RegisterDeviceForm):

    class Meta:
        model = UserDevice
        fields = ('dev_id', 'reg_id', 'name', 'model_name', )


class AdminMessageForm(forms.Form):

    ACTIONS = [
        ('disable_camera', 'Disable camera'),
        ('enable_camera', 'Enable camera'),
        ('password_lock', 'Password lock'),
    ]

    device = forms.CharField(required=True)
    action = forms.ChoiceField(required=True, choices=ACTIONS)
    password = forms.CharField(required=False)
