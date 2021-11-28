from pytube import YouTube

#Intro Welcome - Introduction printed at the beggining
print("")
print("################################################")
print("  ---Welcome to YouTube Downloader 1.0---")
print("")
print("    ---Created by Efe Suner - 2021---")
print("################################################")

print("")

#get link input
link = input("Enter the URL link: ")
yt = YouTube(link)

print("\n")

#stream all the format available for the video
videos = yt.streams.all()

#the index all the format in list (starts -> zero) 
video = list(enumerate(videos))

for i in video:
    print(i)

print("\n\nPlease select the desired option to download the format: ")
dwOption = int(input("--> "))

#ask user which format wanted for the download
dwVideo = videos[dwOption]
#download
dwVideo.download()

print("")
print("###############################")
print("   Successfully downloaded!")
print("###############################")
