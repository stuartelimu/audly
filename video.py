from __future__ import unicode_literals
from twilio.rest import Client
import youtube_dl
import os

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

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
    info_dict = ydl.extract_info('https://www.youtube.com/watch?v=w02I0WzruI0', download=True)
    video_title = info_dict.get('title', None)
    video_ext = info_dict.get('ext', None)

    # formats = info_dict['formats']
    # formattt = formats[0]


    # ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

cwd = os.getcwd()

filename = f"{video_title}.{video_ext}"

# file_size = os.path.getsize(os.path.abspath(os.path.join(cwd, filename)))

print(os.path.abspath(os.path.join(cwd, filename)))


print(cwd)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+256702423277'

client.messages.create(
                        media_url=[filename],
                        body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

# print(formattt)
# print(file_size)

# get recent download and send
