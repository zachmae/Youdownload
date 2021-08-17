from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

def OpenFolder():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        folder_error_message.config(text=Folder_Name, fg="green")
    else:
        folder_error_message.config(text="Select Folder (C:\ if none)", fg="green")

def DownloadVid():
    global Folder_Name
    choice = select_choice.get()
    url = entry_box.get()
    if len(url) > 1:
        error_msg_entry_box.config(text="")
        yt = YouTube(url)
        if choice == options[0]:
            stream = yt.streams.get_highest_resolution()
        elif choice == options[1]:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').last()
        elif choice == options[2]:
            stream = yt.streams.filter(only_audio=True).first()
        else:
            error_msg_entry_box.config(text="Put URL again please", fg="red")
    if Folder_Name == "": Folder_Name = "C:\\"
    stream.download(Folder_Name)
    error_msg_entry_box.config(text="Download completed", fg="green")


dark_mode="#1F1B24"
win = Tk()
win.title("Youdownload")
win.geometry("350x280")
logo = PhotoImage(file = 'youdownload_bubble.png')
win.iconphoto(False, logo)
win.resizable(False, False)
win.configure(bg=dark_mode)
win.columnconfigure(0, weight = 1)

enter_url_label = Label(win, text="Enter the link to the video", fg="white", bg=dark_mode, font=("jost", 15))
enter_url_label.grid()

entry_link = StringVar()
entry_box = Entry(win, width = 50, textvariable=entry_link)
entry_box.grid()

error_msg_entry_box = Label(win,text="Please enter an url", fg="red", bg=dark_mode, font=("jost", 10))
error_msg_entry_box.grid()

save_file_label = Label(win, text="Select save folder", fg="white", bg=dark_mode, font=("jost", 15, "bold"))
save_file_label.grid()

folder_Button = Button(win, width=10, bg="red", fg="white", text="Select folder", command=OpenFolder)
folder_Button.grid()

folder_error_message = Label(win, text="No path selected (default current)", fg="red", bg=dark_mode, font=("jost", 15))
folder_error_message.grid()

download_method_label = Label(win, text="download method", fg="white", bg=dark_mode, font=("jost", 15))
download_method_label.grid()

options = ["Higher Quality", "Lowest Quality", "Audio Only"]
select_choice = ttk.Combobox(win, values=options)
select_choice.grid()

download_button = Button(win, text="Launch Download", width=20, bg="red", fg="white", command=DownloadVid)
download_button.grid()

sources = Label(win, text="Made By Zacharie Lawson", fg="white", bg=dark_mode, font=("jost", 15))
sources.grid()

win.mainloop()