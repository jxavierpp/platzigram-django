"""Platzigram views module."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_word(request):
    """Return a greeting."""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse("Oh, hi! Current server time is {now}".format(now=now))

def hi(request):
    """Hi"""
    numbers = [int(number) for number in request.GET['numbers'].split(",")]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfuly.'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
