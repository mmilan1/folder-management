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

def openDir():
    selectedDir = filedialog.askdirectory()
    #print("Selected directory is:", selectedDir)
    outputStr = "The selected directory is: " + selectedDir
    
    textBlock = Text(window, height=1, width=120 )
    textBlock.insert(END, outputStr)

    textBlock.pack(pady=150)


# button layout created

mainButton = Button(window, text='Open Path', width=30, justify='left', command=openDir)
mainButton.pack()
mainButton.place(x=140, y=70)


window.mainloop()