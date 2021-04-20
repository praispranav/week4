from django.forms import ModelForm
from .models import carreview

class reviewform(ModelForm):
    class Meta:
        models = 'carreview'
        fields = '__all__'