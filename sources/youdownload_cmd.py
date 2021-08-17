from pytube import YouTube

def get_video():
    link = input("Enter the link of the youtube video:  ")
    if link == "exit" or link == "Quit": exit(print("Quitting..."))
    try:
        video = YouTube(link)
        print("Title of the video: ", video.title)
        print("Video by: ", video.author)
        return video
    except: 
        print("Error: couldn't find the video")
        return None

def select_by_tag(stream):
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll available options for downloads:\n")
    for i in range(0,len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1,") ",st[1]," and ",st[3],sep='')
    tag = int(input("\nEnter the itag of your preferred stream to download:   "))
    if tag == "exit" or tag == "Quit": exit(print("Quitting..."))
    ys = yt.streams.get_by_itag(tag)
    return ys

while 1:
    validated = False
    while not validated: 
        yt = get_video()
        answer = input("Is This the good video (Y/N) ?  ").lower()
        if answer == "exit" or answer == "Quit": exit(print("Quitting..."))
        if answer == "y" or answer == "yes": validated = True
    validated = False
    while not validated:
        video_format = input("Do you want to select a custom flux (enter \"custom\"), audio only (enter \"audio\") or best video quality (enter \"video\"): ").lower()
        if video_format == "video":
            ys = yt.streams.get_highest_resolution()
            validated = True
        elif video_format == "audio":
            ys = select_by_tag(str(yt.streams.get_audio_only()))
            validated = True
        elif video_format == "custom":
            ys = select_by_tag(str(yt.streams.filter(progressive=True)))
            validated = True
        elif video_format == "exit" or video_format == "Quit": exit(print("Quitting..."))
    print("###################################\tDownloading...\t###################################")
    ys.download()
    print("\nDownload completed!!")
    print()
    answer = input("Do You want to download another video (Y/N) ?   ").lower()
    if answer == "n" or answer == "no":
        break