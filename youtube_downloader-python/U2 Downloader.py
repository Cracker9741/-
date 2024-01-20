from re import T
from matplotlib.pyplot import clabel
from pytube import YouTube
import tkinter as tk
import os
import io
import urllib.request
from urllib.request import urlopen

from PIL import ImageTk
import PIL

from tkinter import *
import tkinter as tk

import threading

def DownloadButtonOnClick():
    if var.downloading:
        Error("你還沒下載完")

    else:
        ytImg()

def ytImg():
    try:
        ytUrl = tkVar.entry.get()
        yt = YouTube(ytUrl)
        TitleImg_url = yt.thumbnail_url
    except:
        TitleImg_url = "https://images-wixmp-530a50041672c69d335ba4cf.wixmp.com/templates/image/5bf41cca049f03cdc7e842db2201172d6cc1a6b173e8db293a3b880ecc5836561616582409012.jpg"

    image_bytes = urlopen(TitleImg_url).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = PIL.Image.open(data_stream)
    pil_image_resized = pil_image.resize((110, 90), PIL.Image.ANTIALIAS) 

    global tk_image
    tk_image = tk.Label(master=tkVar.window)
    tk_image.photo = ImageTk.PhotoImage(pil_image_resized)
    
    label_pic = tk.Label(tkVar.window, image=tk_image.photo, bg='black')
    label_pic.configure(image=tk_image.photo)
    label_pic.grid(row=1, column=0)

    t = threading.Thread(target=DownloadMp4)
    t.start()


def DownloadMp4():
    try:
        var.downloading = True
        for i in range(5):
            var.textLine[i] = ""

        path = tkVar.pathEntry.get()

        yt = YouTube(tkVar.entry.get(), on_progress_callback=onProgress)
        
        video = yt.streams.get_highest_resolution()
        TextChanger(" ⟸ Download 『" + yt.title + "』:")
        TextChanger("等等啊 ~")

        video.download(str(path))

        TextChanger("Done")
        var.downloading = False

    except:
        if var.first:
            Error("")
        else:
            Error("Error - 檢查您的 路徑 & YouTube 網址")
            var.first = False
        
        var.downloading = False


def TextChanger(SystemStr):
    if(var.textLine[3] != ""):
        for i in range(5):
            var.textLine[i] = ""

    for i in range(5):
        if(var.textLine[i] == ""):
            var.textLine[i] = SystemStr
            break
        
    line1.configure(text = var.textLine[0])
    line2.configure(text = var.textLine[1])
    line3.configure(text = var.textLine[2])
    line4.configure(text = var.textLine[3])
 


def ScheduleText(ScheduleStr):
    var.textLine[2] = ScheduleStr
    line3.configure(text = ScheduleStr)

def Error(ErrorStr):
    lineErr.configure(text = ErrorStr)



def onProgress(stream, chunk, remains):
    total = stream.filesize
    percent = (total-remains) / total * 100
    ScheduleText('下載中… {:05.2f}%'.format(percent))



class var():
    prgRunning = True
    url_IsNormal = False
    
    systemText = ''
    line = 0
    textLine = ["","","","",""]

    downloading = False
    first = True

class tkVar():
    window = tk.Tk()
    window.title('U2ㄅ -only 720p/30fps- Downloader')

    window.geometry("720x180+250+150")
    window.resizable(0,0)
    window.iconbitmap("Icon.ico")

    pathEntry = tk.Entry()
    entry = tk.Entry()

    
ytImg()

label = tk.Label(tkVar.window, text = 'YouTube 網址：\n儲存位置(路徑)：')
label.grid(row=0, column=0)


#==
inputboxFrame = tk.Frame(tkVar.window)
inputboxFrame.grid(row=0,column=1,sticky=NW)


tkVar.pathEntry = tk.Entry(inputboxFrame, width = 80)
tkVar.pathEntry.grid(row=1, column=0)

tkVar.entry = tk.Entry(inputboxFrame, width = 80)
tkVar.entry.grid(row=0, column=0)

button_mp4 = tk.Button(tkVar.window, text = "𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗠𝗣𝟰 - 720p", command = DownloadButtonOnClick)
button_mp4.grid(row=2, column=0)

#==
scheduleLabelFrame = tk.Frame(tkVar.window)
scheduleLabelFrame.grid(row=1,column=1,sticky=NW)

line1 = tk.Label(scheduleLabelFrame,text='')
line1.grid(row=0,column=0,sticky=NW)

line2 = tk.Label(scheduleLabelFrame,text='')
line2.grid(row=1,column=0,sticky=NW)

line3 = tk.Label(scheduleLabelFrame,text='')
line3.grid(row=2,column=0,sticky=NW)

line4 = tk.Label(scheduleLabelFrame,text='')
line4.grid(row=3,column=0,sticky=NW)

lineErr = tk.Label(tkVar.window,text='',fg='red')
lineErr.grid(row=2,column=1)


tkVar.window.mainloop()

#yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')