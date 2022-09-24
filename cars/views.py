from django.shortcuts import render

from cars.forms import CarForm


def index(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()

    return render(request, "index.html", {'form': form})
