from yt_dlp import YoutubeDL
from os.path import expanduser

folderPath = expanduser("~") + "\\Downloads"
videoUrl = "https://www.youtube.com/watch?v=xXNCHYFvAQQ&t=12153s"

with YoutubeDL({
        'format': 'best',
        'outtmpl': folderPath + '/%(id)s.mp4',
        'writesubtitles': True,
 #       'skip_download': True
    }) as ydl:
    ydl.download([videoUrl])
