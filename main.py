#
# main.py - controls the backend of the file management program
#

# ! move instance variable and widget initializations to __init__()

from tkinter import * 
from tkinter import filedialog
from tkinter import ttk
import os
import time

class myApp():
    

    def __init__(self):
        self.window = Tk()
        self.window.title("File Management")
        self.window.geometry("500x350")

        self.askDir = None
        self.selectedDir = ""
        self.outputStr = None
        self.textBlock = Text(self.window, height=1, width=120)

        self.parentFldrOutput = StringVar()
        self.parentFldrOutput.set("")
        self.parentFldrEntry = Entry(self.window, width=20, textvariable=self.parentFldrOutput)
        self.fullPath = ""


        self.dropDown = ttk.Combobox(self.window, values=[1, 2, 3, 4], width=25)

    
    def getSelectedDir(self):
        return self.selectedDir


    #openDirPath() -> open file browsing dialog when open path button is clicked

    def openDir(self):
        self.askDir = filedialog.askdirectory()
        #self.selectedDir = self.askDir
        #print("Selected directory is:", selectedDir)
        self.outputStr = "The selected directory is: " + self.askDir
        
        #self.textBlock = Text(self.window, height=1, width=120)
        self.textBlock.insert('1.0', self.outputStr)

        self.textBlock.place(y=85)

        return self.outputStr

    # updateDir() - called when user clicks button and updates chosen path using openDir()
    def updateDir(self):
        text = self.openDir()
        self.textBlock.delete('1.0', END)
        self.textBlock.insert('1.0', text)
        
    # main button - browse for directory path
    def browseButton(self):
        mainButton = Button(self.window, text='Browse Path', width=20, justify='center', command=self.updateDir)
        mainButton.place(x=175, y=30)
        #mainButton.place(x=140, y=70)
    
    def setSelectedDir(self):

        self.selectedDir = self.askDir
        print(self.selectedDir)

    # button-click event to submit final path to self.selectedDir
    def submitPathButton(self):

        button1 = Button(self.window, text='Enter Path', width=20, command=self.setSelectedDir)
        button1.place(x=175, y=110)

    def createParentFolder(self): # TODO save parent folder entry to self.parentFldrOutput var
        label1 = Label(self.window, text="Enter parent folder name:", justify="left")
        label1.place(x=30, y=142.5)

        self.parentFldrEntry.place(x=185, y=145)

        enterParent = Button(self.window, text="Enter", command=self.getParentFolderName)
        enterParent.place(x=320, y=140)
        
        # Print out the directory here

    def getParentFolderName(self):
        pFolder = self.parentFldrOutput.get()
        print("This is the parent folder name:", pFolder)
        self.fullPath = self.askDir + "/" + pFolder
        print("Full path:", self.fullPath)
        
    def dropDownMenu(self):
        
        self.dropDown.set("How many sub-folders?")
        self.dropDown.place(x=163, y=180)

    def startApp(self): # runs mainloop method
        self.window.mainloop()
        print("\n\033[91mCLEARING SCREEN...\033[0m") # runs once self.window.mainloop() has been executed
        time.sleep(0.85)
        print("\033c", end="") # clear terminal

if __name__ == "__main__":
    m = myApp()
    m.browseButton()
    m.submitPathButton()
    m.createParentFolder()
    #print("dir:", m.getSelectedDir())
    m.dropDownMenu()
    m.startApp()
    