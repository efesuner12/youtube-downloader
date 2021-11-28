from pydub import AudioSegment
import youtube_dl
import threading

linksList = []
linksFile = "links.txt"

with open(linksFile, "r") as toDownFile:
    for line in toDownFile:
        linksList.append(line)

def download(link):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = link, 
        download = False
    )

    filename = f"{video_info['title']}.mp3"

    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    
    print("\nDownload complete...\n")


if __name__ == "__main__":
    for link in range(len(linksList)):
        threading.Thread(target = download, args = (linksList[link],)).start()
        #filenames = ['https://www.youtube.com/watch?v=CxnaPa8ohmM&ab_channel=GEazyMusicVEVO']
        #ydl.download(linksList)
