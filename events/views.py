from django.shortcuts import render
from django.http import Http404

from .models import Event
from .getdata import build_check
# Create your views here.

build_check()

def index(request):
    event_list = Event.objects.order_by('event_day')
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)

def detail(request, event_day):
    try:
        event = Event.objects.get(pk=event_day)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'events/detail.html', {'event': event})
