from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Poi, TravelTime
from logic import get_destinations_travel_times
import json

# Create your views here.
def home(request):
    return render(request, 'traveltime/home.html', {'myvar': 'foo'})


def d3_sandbox(request):

    res = get_destinations_travel_times('Salisbury')
    new_json = [
        {
            'properties': {
                'travel_time': x[0],
            },
            'geometry': json.loads(x[1]),
        }
        for x in res
    ]

    # make a json object to pass to template
    c = {
        'data': [{'x': 50.0, 'y': 50.1}, {'x': 62.0, 'y': 60.5},],
        'textData': ['hello 1', 'foo', 'bar'],
        'myvar': 'foo',
        'pois': json.dumps(new_json),
    }
    return render(request, 'traveltime/graph1.html', c)


def d3_async_pois(request):

    if request.GET:
        html = "<html><body>GET object is %s</body></html>" % str(request.GET)
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("No GET")