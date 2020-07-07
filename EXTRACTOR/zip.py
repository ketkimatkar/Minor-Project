import tkinter as tk
from zipfile import ZipFile
from tkinter import filedialog
from tkinter.messagebox import showinfo
def selectFile():
    global _zip
    _zip=filedialog.askopenfile()
    file=tk.Label(win,text=_zip.name)
    file.grid(row=1,column=0,padx=8)
    return _zip
def saveLocation():
    global savepath
    savepath=filedialog.askdirectory()
    file = tk.Label(win, text=savepath)
    file.grid(row=3, column=0, padx=8)
    return savepath
def extract():
    zf=ZipFile(_zip.name,'r')
    zf.extractall(savepath)
    zf.close()
    showinfo("Success","File Extracted Successfully")
win=tk.Tk()
label1=tk.Label(win,text="Choose Zip File")
label1.grid(row=0,column=0,padx=8,pady=8)
button1=tk.Button(win,text="Choose File",command=selectFile)
button1.grid(row=0,column=1,padx=8,pady=8)
label2=tk.Label(win,text="Where to Extract")
label2.grid(row=2,column=0,padx=8,pady=8)
button2=tk.Button(win,text="Choose Location",command=saveLocation)
button2.grid(row=2,column=1,padx=8,pady=8)
button3=tk.Button(win,text="Extract",command=extract)
button3.grid(row=4,column=0,padx=8,pady=8)
win.mainloop()
