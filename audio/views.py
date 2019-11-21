from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from twilio.twiml.messaging_response import MessagingResponse, Message
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
    req = request.body
    # video_url = req.get('queryResult').get('parameters')['url']
    # song = get_song_details(video_url)
    # print(song)
    # fullfillmentText = {'fulfillmentText': song}
    response = MessagingResponse()

    msg = response.message("hello")
    img = "https://images.unsplash.com/photo-1573258759625-f40df05cfee3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"
    msg.media(img)
    print(req)

    return HttpResponse(response)

