import tkinter
from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry('470x200')
root.configure(bg='#202020')
root.resizable(0,0)
root.title("Youtube Video Downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold' , bg='#202020' , fg='#ffffff').pack()
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold', bg='#202020' , fg='#ffffff').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70, bg='#121212', fg='#ffffff' , textvariable = link).place(x = 32, y = 90)
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15', bg='#202020' , fg='#ffffff').place(x= 175 , y = 170)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' , bg='#ff0303' , fg='#ffffff' , padx = 2, command = Downloader).place(x=180 ,y = 130)
root.mainloop()
