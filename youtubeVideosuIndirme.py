#ilk olarak terminale gidip şu kodu yazın: pip install youtube_dl

#Ve şimdi de python projenizi açıp aşağıdaki kodları yazın, istediğiniz videonun linkini girebilirsiniz. Standart kalitede (720p) indirecektir.

from __future__ import unicode_literals
import youtube_dl

ydl_options = {}

with youtube_dl.YoutubeDL(ydl_options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=yV3LwbO3PPk'])
