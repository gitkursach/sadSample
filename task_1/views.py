from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from .models import *


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class HomePage(View):
    def get(self, request):
        informations = AutoShow_v2.objects.all()
        context = {
            'informations': informations,
            'title': "Главная",
        }
        # return HttpResponseRedirect(request.path)
        return render(request, 'task_1/index.html', context=context)

    def post(self, request):


        context = {
            'title': "Главная",
        }
        return render(request, 'task_1/index.html', context=context)


def edit_line(request, pk):
    get_email = request.POST.get('email')
    get_motor = request.POST.get('motor')
    get_date_birth = request.POST.get('date_birth')
    get_brand = request.POST.get('brand')
    get_appointments = request.POST.getlist('appointment')
    get_providers = request.POST.getlist('provider')

    print(get_email, get_motor, get_date_birth, get_brand, get_appointments, get_providers)
    data = AutoShow_v2.objects.get(pk=pk)
    data.email = get_email
    data.motor = get_motor
    data.date_birth = get_date_birth
    data.brand = get_brand
    data.appointment = get_appointments
    data.provider = get_providers
    data.save()
    return HttpResponseRedirect(reverse_lazy("home"))


def add_line(request):
    print("add_line_v2  ", request.POST)
    get_email = request.POST.get('email')
    get_motor = request.POST.get('motor')
    get_date_birth = request.POST.get('date_birth')
    get_brand = request.POST.get('brand')
    get_appointments = request.POST.getlist('appointment')
    get_providers = request.POST.getlist('provider')

    add_auto = AutoShow_v2(email=get_email, motor=get_motor, date_birth=get_date_birth, brand=get_brand,
                           appointment=get_appointments, provider=get_providers)
    add_auto.save()

    return HttpResponseRedirect(reverse_lazy("home"))


def delete_line(request, pk):
    delete_line = AutoShow_v2.objects.get(pk=pk)
    delete_line.delete()
    return HttpResponseRedirect(reverse_lazy("home"))

def delete_all(request):
    delete_all = AutoShow_v2.objects.all()
    delete_all.delete()
    return HttpResponseRedirect(reverse_lazy("home"))