from django import forms

from cars.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['km_of_car', 'event_text', 'periodic_event', 'next_date', 'next_change']
