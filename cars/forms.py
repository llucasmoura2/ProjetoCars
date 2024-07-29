from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta():
        model = Car
        fields = '__all__'


    def clean_factory_year(self):
       factory_year = self.cleaned_data.get('factory_year')
       if factory_year < 1975:
          self.add_error('factory_year', 'Não é possivel cadastrar carros que são fabricados antes de 1975!')
       return factory_year
