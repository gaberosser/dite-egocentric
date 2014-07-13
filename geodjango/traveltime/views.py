from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.renderers import JSONRenderer
from models import Poi, TravelTime
from logic import get_destinations_travel_times
import json
import datetime
import random
from django.views.decorators.csrf import csrf_exempt


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


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


def d3_sandbox2(request):
    c = {
        'myvar': 'foo',
    }
    # random spacetime data
    n = 10
    res = []
    for i in range(n):
        t = datetime.datetime.now()
        res.append((t, random.random(), random.random()))

    return render(request, 'traveltime/graph2.html', c)

@csrf_exempt
def create_data(request):
    # create random spacetime data
    if request.method == 'POST':
        n = int(request.POST.get('n', '10'))
    else:
        n = 10

    res = []
    for i in range(n):
        t = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))
        res.append((t.strftime("%Y-%m-%d %H:%M:%S.") + "%03d" % int(t.microsecond / 1000.), random.random(), random.random()))
    # return JSONResponse(json.dumps(res))
    return JSONResponse(res)


def d3_async_pois(request):

    if request.GET:
        html = "<html><body>GET object is %s</body></html>" % str(request.GET)
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("No GET")