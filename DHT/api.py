import asyncio

import vonage
from telegram import Bot

from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import rest_framework
#alerte
from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import rest_framework




@api_view(["GET","POST"])
def dhtser(request):
    if request.method=="GET":
        all=Dht11.objects.all()
        dataSer=DHT11serialize(all,many=True)
        return Response(dataSer.data)
    elif request.method=="POST":
        serial=DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.id, status=status.HTTP_400_CREATED)

#################"




###############""



#alerte


@api_view(["GET","POST"])
def dhtser(request):
    if request.method=="GET":
        all=Dht11.objects.all()
        dataSer=DHT11serialize(all,many=True) # les donnée se form fichier
        return Response(dataSer.data)
    elif request.method=="POST":
        serial=DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            derniere_temperature = Dht11.objects.last().temp
            print(derniere_temperature)
            if (int(derniere_temperature) > 30):
                subject = 'Alerte DHT'
                message = 'Attention, la temperature de votre local depasse la limite'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['ibrahime.chaine@gmail.com','zakariabouaid03@gmail.com']
                send_mail(subject, message, email_from, recipient_list)
                ##############
                telegram_alert(request,message)

                client = vonage.Client(key="6f191935", secret="KUv0Ff8fZ3ChGlij")
                client.sms.send_message(
                    {
                        "from": "Alerte",
                        "to": "212707026926",
                        "text": f"Il y a une alerte importante sur votre Capteur, la température est: {Dht11.objects.last().temp} et dépasse le seuil.",
                    })

                return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.id, status=status.HTTP_400_CREATED)


# Alerttelegrame
def telegram_alert(request,message):
    async def send_telegram_message(token, chat_id, message_text):
        bot = Bot(token=token)
        await bot.send_message(chat_id=chat_id, text=message_text)

    bot_token = '6643865651:AAHFxNZsUFN9w0lh9q_BW4xl9cvaJFL1pwU'
    chat_id = '1778427259'
    message_text = message

    asyncio.run(send_telegram_message(bot_token, chat_id, message_text))

# AlertSMS


