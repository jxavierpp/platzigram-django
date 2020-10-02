"""Platzigram views module."""

from django.http import HttpResponse


def hello_word(request):
    """Return a greeting."""
    return HttpResponse('Hello World!')