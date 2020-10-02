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

def sorted_numbers(request):
    """Sort numbers."""
    numbers = [int(number) for number in request.GET['numbers'].split(",")]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfuly.'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
         message = "Hi {}, Welcome to Platzigram!.".format(name)
    return HttpResponse(message)
