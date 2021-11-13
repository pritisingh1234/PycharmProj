from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader

from .models import Employees


def hello(request):
    ac = Employees.objects.all()
    template = loader.get_template('Home.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request,e_name):
    try:
        ename = Employees.objects.get(pk=e_name)
    except Employees.DoesNotExist:
        raise Http404("Employee Does Not Exist")
    return (request, 'detail.html')


# To generate 404 error if user try to check unregistered user


