from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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


<<<<<<< HEAD
=======
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


>>>>>>> f1089612de8c70c6db8ed8f2c96c39886a704d00

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



