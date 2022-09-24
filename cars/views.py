from django.shortcuts import render
from django.views.generic import ListView

from cars.forms import CarForm
from cars.models import Car


def index(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()

    return render(request, 'index.html', {'form': form})


class CarsListView(ListView):
    model = Car
    template_name = 'car-list.html'
