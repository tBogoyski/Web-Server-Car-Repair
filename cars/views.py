from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView

from cars.forms import CarForm
from cars.models import Car


class IndexView(TemplateView):
    template_name = 'index.html'


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'add-car.html'
    success_url = reverse_lazy('car_list')


class CarListView(ListView):
    model = Car
    template_name = 'car-list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car-details.html'


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
    template_name = 'delete-car.html'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'edit-car.html'
    success_url = reverse_lazy('car_list')
