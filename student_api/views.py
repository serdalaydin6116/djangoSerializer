from django.shortcuts import render, HttpResponse, get_object_or_404


def home(request):
    return HttpResponse('<h1>API Page</h1>')
