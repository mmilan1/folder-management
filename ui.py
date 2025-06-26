#
# ui.py - Basic UI for managing files
#

import tkinter
from tkinter import filedialog

window = tkinter.Tk()
window.title("File Management")
window.geometry("400x350")

displayPath = tkinter.Text(window, height=10)
#displayPath.grid(column=0, row=0, sticky='nsew')


#openDirPath() -> open file browsing dialog when open path button is clicked

def openDirPath():
    selectedDir = filedialog.askdirectory()

# button layout created

mainButton = tkinter.Button(window, text='Open Path', width=30, justify='left', command=openDirPath)
mainButton.pack()
mainButton.place(x=90, y=70)


window.mainloop()