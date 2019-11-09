from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from twilio.rest import Client
import youtube_dl
import os

def home(request):
    return HttpResponse("Hello world!")

def get_song_details(url):
    # get song details of url

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)

        video_title = info_dict.get('title', None)
        video_ext = info_dict.get('ext', None)

    return f"{video_title}.mp3"

@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    video_url = req.get('queryResult').get('parameters')['url']
    song = get_song_details(video_url)
    print(song)
    fullfillmentText = {'fulfillmentText': song}
    return JsonResponse(fullfillmentText, safe=False)

