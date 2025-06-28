#
# ui.py - Basic UI for managing files
#

from tkinter import * 
from tkinter import filedialog

window = Tk()
window.title("File Management")
window.geometry("500x350")

displayPath = Text(window, height=10)
#displayPath.grid(column=0, row=0, sticky='nsew')


#openDirPath() -> open file browsing dialog when open path button is clicked

def openDirPath():
    selectedDir = filedialog.askdirectory()
    #print("Selected directory is:", selectedDir)
    outputStr = "The selected directory is: " + selectedDir
    text = Label(window, width=120, borderwidth=2, text=outputStr, anchor=CENTER, wraplength=250)
    text.pack(pady=120)

# button layout created

mainButton = Button(window, text='Open Path', width=30, justify='left', command=openDirPath)
mainButton.pack()
mainButton.place(x=140, y=70)


window.mainloop()