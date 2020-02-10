from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from django.db.models import Q

from .models import Car
from .forms import CarForm


def my_list(request):
    form = CarForm()
    if not list(request.GET.items()):
        cars_list = Car.objects.all()
        return render(request, 'my_list.html', {'form': form, 'car_list': cars_list})
    else:
        cars_list = Car.objects.filter(Q(brand=request.GET.get('brand')) & Q(year__gt=request.GET.get('year')) & Q(transmission=request.GET.get('transmission')))
        return render(request, 'my_list.html', {'form': form, 'car_list': cars_list})
   