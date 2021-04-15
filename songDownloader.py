from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3
import urllib.request
import re
from PIL import ImageTk,Image


Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        url=url.replace(' ', "+")
        search_keyword =url
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        name="https://www.youtube.com/watch?v=" + video_ids[0]
        yt = YouTube(name)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()


        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Paste Link again!!", fg="red")
        ytdchoices.configure(state=DISABLED)


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")





root = Tk()
root.title("MELODY")
root.configure(bg='azure')
root.iconbitmap('melody.ico')
root.geometry("550x600") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="Enter song name",bg='azure',font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,fg="red",bg='azure',font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",bg='azure',font=("jost",15))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(root,fg="red",bg='azure',font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",bg='azure',font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()


#donwload btn
downloadbtn = Button(root,text="Donwload",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()


root.mainloop()