from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView

from cars.forms import EventForm
from cars.models import Car, Event


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(car_id=self.object.id)
        return context


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
    template_name = 'delete-car.html'


class CarUpdateView(UpdateView):
    model = Car
    fields = ['name', 'model', 'maker', 'year_of_make', 'registration_number']
    template_name = 'edit-car.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('car_detail', args=(self.object.id,))


def add_event_to_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.car = car
            event.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = EventForm()
    return render(request, 'add-event.html', {'form': form, 'car': car})
