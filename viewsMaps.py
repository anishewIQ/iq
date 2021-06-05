__author__ = 'Andrey'
__copyright__ = 'Copyright 2021, IQ-Beat'
__contact__ = 'azhestyannikovs@edu.hse.ru'

import json

from django.shortcuts import render
from django.views import View

import iqb.loggers as loggers

from .utils import Params, HttpResponse

logger = loggers.setup_logger('lk', __file__)


class MapsView(View):
    def get(self, request, *args, **kwargs):
        u = request.user
        p = Params()
        p.setup_struct(u)
        p.setup_perms(u)

        emp_geodata = {}
        date = datetime.now()
        query = GeoEvent.objects.all().filter(actual_time__day=date.day, actual_time__month=date.month)
        for ev in query:
            if emp_geodata.get(ev.emp_id) is None:
                emp_geodata[ev.emp_id] = []
            emp_geodata[ev.emp_id].append([ev.lat, ev.lon])
        p.params['emp_geodata'] = emp_geodata

        return render(request, 'maps.html', p.make())

