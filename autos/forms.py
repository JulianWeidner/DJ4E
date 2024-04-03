from autos.models import Make, Autos
from django.forms import ModelForm


class MakeForm(ModelForm):
    class Meta():
        model = Make
        fields = '__all__'

class AutosForm(ModelForm):
    class Meta():
        model = Autos
        fields = '__all__'



