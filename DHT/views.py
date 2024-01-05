import datetime
from django.utils import timezone
from django.shortcuts import render
from .models import Dht11
from django.db.models import Count, Q
from django.shortcuts import render
from django.http import HttpResponse
import csv


#affichage de la table
def table(request):
    derniere_ligne = Dht11.objects.last()
    derniere_date = Dht11.objects.last().dt
    delta_temps = timezone.now() - derniere_date
    difference_minutes = delta_temps.seconds // 60
    temps_ecoule = ' il y a ' + str(difference_minutes) + ' min'
    if difference_minutes > 60:
        temps_ecoule = 'il y ' + str(difference_minutes // 60) + 'h' + str(difference_minutes % 60) + 'min'
    valeurs = {'date': temps_ecoule, 'id': derniere_ligne.id, 'temp': derniere_ligne.temp, 'hum': derniere_ligne.hum}
    return render(request, 'table.html', {'valeurs': valeurs})

########################afiichage CSV#############################################################################################################"
def download_csv(request):
    model_values = Dht11.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dht.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'temp', 'hum', 'dt'])
    liste = model_values.values_list('id', 'temp', 'hum', 'dt')
    for row in liste:
        writer.writerow(row)
    return response


def csv_jour(request):
    now = timezone.now()
    last_24_hours = now - timezone.timedelta(hours=24)
    model_values = Dht11.objects.filter(dt__range=(last_24_hours, now))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dhtJOUR.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'temp', 'hum', 'dt'])
    liste = model_values.values_list('id', 'temp', 'hum', 'dt')
    for row in liste:
        writer.writerow(row)
    return response



def csv_semaine(request):
    date_debut_semaine = timezone.now().date() - datetime.timedelta(days=7)
    print(datetime.timedelta(days=7))
    print(date_debut_semaine)
    model_values =  Dht11.objects.filter(dt__gte=date_debut_semaine)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dhtSEMAINE.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'temp', 'hum', 'dt'])
    liste = model_values.values_list('id', 'temp', 'hum', 'dt')
    for row in liste:
        writer.writerow(row)
    return response

def csv_mois(request):
    dht = Dht11.objects.all()
    date_debut_semaine = timezone.now().date() - datetime.timedelta(days=30)
    print(datetime.timedelta(days=30))
    print(date_debut_semaine)
    model_values =  Dht11.objects.filter(dt__gte=date_debut_semaine)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dhtMOIS.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'temp', 'hum', 'dt'])
    liste = model_values.values_list('id', 'temp', 'hum', 'dt')
    for row in liste:
        writer.writerow(row)
    return response
########################afiichage HUMIDITE#############################################################################################################"

def chartHUM(request):
    tab=Dht11.objects.all()
    s={'tab':tab}
    return render(request,'chartHUM.html',s)

def chart_HUM_mois(request):
    dht = Dht11.objects.all()
    date_debut_semaine = timezone.now().date() - datetime.timedelta(days=30)
    print(datetime.timedelta(days=30))
    print(date_debut_semaine)
    tab= Dht11.objects.filter(dt__gte=date_debut_semaine)
    s = {'tab': tab}
    return render(request, 'chartHUM.html', s)

def chart_HUM_semaine(request):
    dht = Dht11.objects.all()
    date_debut_semaine = timezone.now().date() - datetime.timedelta(days=7)
    print(datetime.timedelta(days=7))
    print(date_debut_semaine)
    tab = Dht11.objects.filter(dt__gte=date_debut_semaine)
    s = {'tab': tab}
    return render(request, 'chartHUM.html', s)


def chart_HUM_jour(request):
    now = timezone.now()
# Récupérer l'heure il y a 24 heures
    last_24_hours = now - timezone.timedelta(hours=24)
# Récupérer tous les objets de Module créés au cours des 24 dernières
    tab= Dht11.objects.filter(dt__range=(last_24_hours, now))
    s = {'tab': tab}
    return render(request, 'chartHUM.html', s)

########################afiichage TEMERATURE#############################################################################################################"

def chartTEMP(request):
    tab=Dht11.objects.all()
    s={'tab':tab}
    return render(request,'chartTEMP.html',s)



def chart_TEMP_jour(request):
    now = timezone.now()
# Récupérer l'heure il y a 24 heures
    last_24_hours = now - timezone.timedelta(hours=24)
# Récupérer tous les objets de Module créés au cours des 24 dernières
    tab= Dht11.objects.filter(dt__range=(last_24_hours, now))
    s = {'tab': tab}
    return render(request, 'chartTEMP.html', s)


def chart_TEMP_semaine(request):
    dht = Dht11.objects.all()
    date_debut_semaine = timezone.now().date() - datetime.timedelta(days=7)
    print(datetime.timedelta(days=7))
    print(date_debut_semaine)
    tab = Dht11.objects.filter(dt__gte=date_debut_semaine)
    s = {'tab': tab}
    return render(request, 'chartTEMP.html', s)

def chart_TEMP_mois(request):
    dht = Dht11.objects.all()
    date_debut_semaine = timezone.now().date() - datetime.timedelta(days=30)
    print(datetime.timedelta(days=30))
    print(date_debut_semaine)
    tab= Dht11.objects.filter(dt__gte=date_debut_semaine)
    s = {'tab': tab}
    return render(request, 'chartTEMP.html', s)



