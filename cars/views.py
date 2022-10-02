from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView

from cars.models import Car


class IndexView(TemplateView):
    template_name = 'index.html'


class CarCreateView(CreateView):
    model = Car
    fields = ['name', 'model', 'maker', 'year_of_make', 'registration_number']
    template_name = 'add-car.html'
    success_url = reverse_lazy('car_list')


class CarListView(ListView):
    model = Car
    template_name = 'car-list.html'

    def get_queryset(self):
        return Car.objects.order_by('-created_date')


class CarDetailView(DetailView):
    model = Car
    template_name = 'car-details.html'


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
    template_name = 'delete-car.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['name', 'model', 'maker', 'year_of_make', 'registration_number']
    template_name = 'edit-car.html'
    success_url = reverse_lazy('car_list')
