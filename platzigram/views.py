"""Platzigram views module."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


def hello_word(request):
    """Return a greeting."""
    return HttpResponse('Hello World!')