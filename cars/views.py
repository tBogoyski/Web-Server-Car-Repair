from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cars.forms import CarForm
from cars.models import Car


def index(request):
    return render(request, 'index.html')


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()

    return render(request, 'add-car.html', {'form': form})


class CarListView(ListView):
    model = Car
    template_name = 'car-list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car-details.html'
