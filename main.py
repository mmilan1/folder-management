#
# main.py - controls the backend of the file management program
#

from tkinter import * 
from tkinter import filedialog
from tkinter import ttk

class myApp():
    

    def __init__(self):
        self.window = Tk()
        self.window.title("File Management")
        self.window.geometry("500x350")

        self.selectedDir = None
        self.outputStr = None
        self.textBlock = Text(self.window, height=1, width=120)

        self.dropDown = ttk.Combobox(self.window, values=[1, 2, 3, 4], width=25)


    #openDirPath() -> open file browsing dialog when open path button is clicked

    def openDir(self):
        self.selectedDir = filedialog.askdirectory()
        #print("Selected directory is:", selectedDir)
        self.outputStr = "The selected directory is: " + self.selectedDir
        
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
    def button(self):
        mainButton = Button(self.window, text='Open Path', width=20, justify='center', command=self.updateDir)
        mainButton.place(x=175, y=30)
        #mainButton.place(x=140, y=70)

    def createParentFolder(self):
        
        label1 = Label(self.window, text="Enter parent folder name:", justify="left")
        label1.place(x=30, y=122.5)
        parentButton = Entry(self.window, width=20)
        parentButton.place(x=189, y=125)

        
    def dropDownMenu(self):
        
        self.dropDown.set("How many sub-folders?")
        self.dropDown.place(x=160, y=180)

    def startApp(self):
        self.window.mainloop()


if __name__ == "__main__":
    m = myApp()
    m.button()
    m.createParentFolder()
    m.dropDownMenu()
    m.startApp()
    print("dir:", m.selectedDir)