from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import os
text=''
def which_button(m):
    global text
    text=m
    print(text)
    
def download():
    global text
    print(text)
    if text=='video' or text=='':
        vdownload()
    else:
        adownload()


def adownload():
    link = e1.get()
    yt = YouTube(link)
    try:
          video = yt.streams.filter(only_audio=True).first()
          out_file = video.download()
          base, ext = os.path.splitext(out_file)
          new_file = base + '.mp3'
          os.rename(out_file, new_file)
          messagebox.showinfo("sucess","Audio has been Downloaded")
          e1.delete(0,END)
    except:
        messagebox.showwarning("OOPS", "Download failed")
    

def vdownload():
    link = e1.get()
    video = YouTube(link)
    try:
         stream = video.streams.get_highest_resolution()
         stream.download()
         messagebox.showinfo("sucess","Video has been Downloaded")
         e1.delete(0,END)
    except:
        messagebox.showwarning("OOPS", "Download failed")

root=Tk()
root.geometry("600x400+100+100")
root.title("Video and Audio Downloader")
root.config(background="#e4eaf5")
# i=IntVar()
frame=Frame(root,width=600,height=100)
variable = StringVar()
audiob=Button(frame,text="Audio",font=("Baloo Bhai",13),bg="#8490a3",width=10 ,highlightcolor='white', command=lambda m="audio": which_button(m))
videob=Button(frame,text="Video",font=("Baloo Bhai",13),bg="#8490a3",width=10, command=lambda m="video": which_button(m))
audiob.pack(side=LEFT)
videob.pack(side=RIGHT)
frame.pack()
l1=Label(root,text="Paste your link here!",font=("Girassol",20), bg="#e4eaf5" ,fg="#8490a3")
l1.pack(pady=(30,0))
e1=Entry(root,width=40,font=("Baloo Bhai",10))
e1.pack(pady=(20,0))
b1=Button(root,text="Download",font=("Baloo Bhai",13),bg="#8490a3",width=10,command=download)
b1.pack(pady=(20,0))
root.mainloop()


