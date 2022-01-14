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
        informations = AutoShow.objects.all()
        appointments = Appointment.objects.all()
        providers = Provider.objects.all()
        test = ['qwe,q22,qew', '123,321,sdrf', 'dsds,sdds,dsdwsed']
        context = {
            'test': test,
            'appointments': appointments,
            'providers': providers,
            'informations': informations,
            'title': "Главная",
        }
        # return HttpResponseRedirect(request.path)
        return render(request, 'task_1/index.html', context=context)

    def post(self, request):
        get_first_name = request.POST.get('first_name')

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

    edit_auto = AutoShow.objects.get(pk=pk)
    edit_auto.email = get_email
    edit_auto.motor = get_motor
    edit_auto.date_birth = get_date_birth
    edit_auto.brand = get_brand
    edit_auto.save()

    edit_appoints = Appointment.objects.filter(appointment=pk)
    if len(edit_appoints) < len(get_appointments):
        delete_appointments = Appointment.objects.filter(appointment=pk)
        for delete_appointment in delete_appointments:
            delete_appointment.delete()
        for get_appointment in get_appointments:
            save_appointment = Appointment(appointment=edit_auto, title_appoint=get_appointment)
            save_appointment.save()
    elif len(edit_appoints) == len(get_appointments):
        print('good')
        for get_appointment, edit_appoint in get_appointments:
                edit_appoint.title_appoint = get_appointment
                edit_appoint.save()


        # for get_provider in get_providers:
        #     edit_providers = Provider.objects.filter(provider=pk)
        #     for edit_provider in edit_providers:
        #         edit_provider.title_appoint = get_provider
        #         edit_provider.save()



    return HttpResponseRedirect(reverse_lazy("home"))

def add_line(request):
    print(request.POST)
    get_email = request.POST.get('email')
    get_motor = request.POST.get('motor')
    get_date_birth = request.POST.get('date_birth')
    get_brand = request.POST.get('brand')
    get_appointments = request.POST.getlist('appointment')
    get_providers = request.POST.getlist('provider')

    add_auto = AutoShow(email=get_email, motor=get_motor, date_birth=get_date_birth, brand=get_brand)
    add_auto.save()
    for get_appointment in get_appointments:
        add_appoint = Appointment(title_appoint=get_appointment, appointment=add_auto)
        add_appoint.save()
    for get_provider in get_providers:
        add_provider = Provider(title_provider=get_provider, provider=add_auto)
        add_provider.save()

    return HttpResponseRedirect(reverse_lazy("home"))