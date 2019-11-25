from __future__ import unicode_literals
from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from twilio.twiml.messaging_response import MessagingResponse, Message
import youtube_dl
import os
from django.conf import settings
from .models import Music

def home(request):
    return HttpResponse("Hello world!")

def get_song_details(url):
    # get song details of url

    ydl_opts = {
        'outtmpl': f'{settings.MEDIA_ROOT}/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)

        video_title = info_dict.get('title', None)
        video_ext = info_dict.get('ext', None)

    ttt = f"{video_title}.mp3"

    f = File(open(f"{settings.MEDIA_ROOT}/{video_title}.mp3", "rb"))
    mm = Music.objects.create(title=ttt, upload=ttt)
    print(mm.upload.url)

    return f"{video_title}.mp3"

@csrf_exempt
def webhook(request):
    # req = request.POST.get('Body')
    # body = request.get('Body', None)
    video_url = request.POST.get('Body')
    song = get_song_details(video_url)
    # print(song)
    # fullfillmentText = {'fulfillmentText': song}
    response = MessagingResponse()

    response.message(song)
    # msg = response.message(request.POST.get('Body'))
    # img = "https://images.unsplash.com/photo-1573258759625-f40df05cfee3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"
    # msg.media(img)
    print(request)

    return HttpResponse(response)

