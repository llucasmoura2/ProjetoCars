from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.


class CarListViews(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = Car.objects.filter(model__icontains = search)
        return cars






"""""
def cars_view(request):
    cars= Car.objects.all().order_by('model')  # .order_by(" - model") a ordenação fica ao contrario 
    search = request.GET.get('search')
    
    if search:
        cars = Car.objects.filter(model__icontains = search)
    
    return render (request, 
                   'cars.html', 
                {'cars':cars}
     )

     #modelo function views pode ser substituido por class views 
     #modelo class view abaixo
"""""

# cars = Car.objects.all()
#cars = Car.objects.filter(brand__name = 'Fiat') #ou "Car.objects.filter(brand = 2)" o id é a posição na tabela sql "foreingkey"
# cars = Car.objects.filter(model = "uno com escada") desse jeito se não for uma ForeingKey
 # cars = Car.objects.filter(model__contains = "chevette") "contains" significa que contem e pode ser uma letra ou palavra 




"""""
class CarsView(View):
    def get(self, request):
        cars= Car.objects.all().order_by('model')  # .order_by(" - model") a ordenação fica ao contrario 
        search = request.GET.get('search')
    
        if search:
            cars = Car.objects.filter(model__icontains = search)
    
        return render(request, 'cars.html', {'cars':cars})

---------------------------------------------------------------------------------------------------------------------------------------


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
       new_car_form = CarModelForm
    return render (request, 'new_car.html', {'new_car_form': new_car_form})

"""""


"""""
class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render (request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render (request, 'new_car.html', {'new_car_form': new_car_form})

"""""

@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class NewCarCreatView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' #manda após o cadastro do carro
    


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


    
@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    

@method_decorator(login_required(login_url= 'login'), name = 'dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'



