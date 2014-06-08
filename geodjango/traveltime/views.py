from django.shortcuts import render
from models import Poi, TravelTime
from logic import get_destinations_travel_times
import json

# Create your views here.
def home(request):
    return render(request, 'traveltime/home.html', {'myvar': 'foo'})


def d3_sandbox(request):

    res = get_destinations_travel_times('Salisbury')

    # make a json object to pass to template
    c = {
        'data': [{'x': 50.0, 'y': 50.1}, {'x': 62.0, 'y': 60.5},],
        'textData': ['hello 1', 'foo', 'bar'],
        'myvar': 'foo',
        'pois': res,
    }
    return render(request, 'traveltime/graph1.html', c)