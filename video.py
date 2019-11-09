from __future__ import unicode_literals
from twilio.rest import Client
import youtube_dl
import os

TWILIO_ACCOUNT_SID = 'ACe0d1aa56ae23fb3775045657146a32aa'
TWILIO_AUTH_TOKEN = '8c3c0782d3e40102c1664fa449b9133f'

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc', download=False)
    video_title = info_dict.get('title', None)
    video_ext = info_dict.get('ext', None)

    # ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

print(f"{video_title}.{video_ext}")

# get recent download and send
