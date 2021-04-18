from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube  # pip install pytube
import urllib.request
import re
import json
import urllib

#from PIL import ImageTk,Image
Folder_Name = ""
#file location
def openLocation():


    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) < 1):
        locationError = Label(root, bg='azure', font=("jost", 15), fg='green')
        locationError.config(text="Please Choose Folder!!", fg="red")

    elif(len(Folder_Name) > 1):
        saveEntry.configure(state=DISABLED)
        locationError=Label(root,bg='azure',font=("jost",15),fg='green')
        locationError.grid()
        locationError.config(text=Folder_Name,fg="green")


        songLabel3 = Label(root, bg='azure')
        songLabel3.grid()



        # Download Quality

        ytdQuality = Label(root, text="Select Quality", bg='azure', font=("jost", 15))
        ytdQuality.grid()
        choices = ["720p", "144p", "Only Audio"]
        global ytdchoices
        ytdchoices = ttk.Combobox(root, values=choices,font=('Helvetica,12'))
        ytdchoices.grid()

        global downloadbtn
        downloadbtn = Button(root, text="Download", width=12,  command= DownloadVideo,font=4)
        downloadbtn.grid()







def search():
    lb8 = Label(root, text="Please enter a song name!", fg='red', bg='azure', font=('Helvetica', 12))
    if(len(ytdEntry.get())<1):

        lb8.grid()
    elif(len(ytdEntry.get())>1):

       b.configure(state=DISABLED)
       choices3=[]

       url = ytdEntry.get()+"songs"
       url = url.replace(' ', "+")
       search_keyword = url
       html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
       video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

       for i in range(8):
           params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_ids[i]}
           url = "https://www.youtube.com/oembed"
           query_string = urllib.parse.urlencode(params)
           url = url + "?" + query_string

           with urllib.request.urlopen(url) as response:
              response_text = response.read()
              data = json.loads(response_text.decode())
              choices3.append(data['title'])
       songLabel1 = Label(root, bg='azure',text="Choose your song!!",fg='brown',font=6)
       songLabel1.grid()

       global  ytdchoices2
       ytdchoices2 = ttk.Combobox(root, values=choices3,width=90,font=('Helvetica',12))
       ytdchoices2.grid()

       songLabel2 = Label(root, bg='azure')
       songLabel2.grid()

       name = "https://www.youtube.com/watch?v=" + video_ids[0]
    # btn to save file
       global saveEntry
       saveEntry = Button(root, text="Choose Path",width=12,font=4, command= openLocation)
       saveEntry.grid()



def DownloadVideo():
    choices = ["720p", "144p", "Only Audio"]
    choice = ytdchoices.get()
    url5 = ytdchoices2.get()
    if(len(url5)>1):







        url5=url5.replace(' ', "+")
        search_keyword =url5
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        name="https://www.youtube.com/watch?v=" + video_ids[0]

        params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_ids[0]}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            print(data['title'])



        yt = YouTube(name)









        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()


        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Paste Link again!!", fg="red")



    #download function
    select.download(Folder_Name)

    songLabel4 = Label(root, bg='azure')
    songLabel4.grid()

    ytdError = Label(root, fg="red", bg='azure',text="!!DOWNLOAD COMPLETED!!", font=("jost", 20))
    ytdError.grid()
    downloadbtn.configure(state=DISABLED)




root = Tk()
root.title("MELODY")
root.configure(bg='azure')
#root.iconbitmap('melody.ico')
root.geometry("900x650") #set window
root.columnconfigure(0,weight=1) # set all content in center.



lb=Label(root,text="!! MELODY !!",bg='azure',font=("helvetica",30),fg='magenta')
lb.grid()

lb1=Label(root,text="Download any song you love for free here.....",bg='azure',font=("helvetica",20),fg='orange')
lb1.grid()

ytdLabel = Label(root,text="Enter song/album/artist name",bg='azure',font=("jost",15))
ytdLabel.grid()



#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=40,textvariable=ytdEntryVar,font=('Helvetica,10'))
ytdEntry.grid()

global b
b=Button(root,text="Search",command=search,width=8,font=6)
b.grid()

songLabel=Label(root,bg='azure')
songLabel.grid()

root.mainloop()
