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
        return render(request, 'maps.html', p.make())

