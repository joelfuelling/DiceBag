from django.forms import ModelForm
from .models import Rolls

class RollsForm(ModelForm):
    class Meta:
        model = Rolls
        fields = ['date', 'result']

# Note that our custom form inherits from ModelForm and has a nested class Meta: #! to declare the Model being used and the fields we want inputs generated for. Confusing? Absolutely, but it's just the way it is, so accept it and sleep well.