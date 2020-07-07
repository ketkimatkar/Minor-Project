import tkinter as tk
from timeit import default_timer as timer
from tkinter.messagebox import showinfo
import random
x=0
def game():
    global x
    if x==0:
        win.destroy()
        x=x+1
    def check():
        if entry.get()==words[word]:
            end=timer()
            print(end-start,"seconds")
        else:
            print("Wrong Spelling!!!!")
    def clear():
        win1.destroy()
        game()
    def Quit():
        win1.destroy()
        showinfo("QUIT","You have quit the game")
        exit()
    words=["programming","coding","helicopter","aeroplane","homosapiens","furniture","biology","youtube","functions","window","operating","america","configuration","terminal","finished","libraries"]
    word=random.randint(0,(len(words)-1))
    start=timer()
    win1=tk.Tk()
    label2=tk.Label(win1,text=words[word],font="times 20")
    label2.grid(row=0,column=1,padx=8,pady=8)
    label3=tk.Label(win1,text="Type the given word in the field box",font="times 20")
    label3.grid(row=1,column=1,padx=8,pady=8)
    entry=tk.Entry(win1)
    entry.grid(row=2,column=1)
    button2 = tk.Button(win1, text="submit",command=check,bg="gray")
    button2.grid(row=3, column=0, padx=8, pady=8)
    button3 = tk.Button(win1, text="try again",command=clear,bg="gray")
    button3.grid(row=3, column=1, padx=8, pady=8)
    button4=tk.Button(win1,text="exit",command=Quit,bg="gray")
    button4.grid(row=3,column=2,padx=8,pady=8)
    win1.mainloop()
win=tk.Tk()
label1=tk.Label(win,text="Let's start the game. Click on Play")
label1.grid(row=0,column=0,padx=8,pady=8)
button1=tk.Button(win,text="PLAY",command=game,bg="gray")
button1.grid(row=2,column=2,padx=8,pady=8)
win.mainloop()