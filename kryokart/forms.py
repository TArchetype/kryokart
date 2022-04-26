from django.forms import ModelForm
from .models import GPS

class GPSForm(ModelForm):
    class Meta:
        model = GPS
        fields = '__all__'