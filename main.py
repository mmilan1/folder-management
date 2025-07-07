#
# main.py - controls the backend of the file management program
#

from tkinter import * 
from tkinter import filedialog

class myApp():
    

    def __init__(self):
        self.window = Tk()
        self.window.title("File Management")
        self.window.geometry("500x350")

        self.selectedDir = None
        self.outputStr = None
        self.textBlock = Text(self.window, height=1, width=120)


    #openDirPath() -> open file browsing dialog when open path button is clicked

    def openDir(self):
        self.selectedDir = filedialog.askdirectory()
        #print("Selected directory is:", selectedDir)
        self.outputStr = "The selected directory is: " + self.selectedDir
        
        #self.textBlock = Text(self.window, height=1, width=120)
        self.textBlock.insert('1.0', self.outputStr)

        self.textBlock.pack(pady=150)

        return self.outputStr

    # updateDir() - called when user clicks button and updates chosen path using openDir()
    def updateDir(self):
        text = self.openDir()
        self.textBlock.delete('1.0', END)
        self.textBlock.insert('1.0', text)
        
    # main button - browse for directory path
    def button(self):
        mainButton = Button(self.window, text='Open Path', width=30, justify='left', command=self.updateDir)
        mainButton.pack()
        mainButton.place(x=140, y=70)

    def startApp(self):
        self.window.mainloop()


if __name__ == "__main__":
    m = myApp()
    m.button()
    m.startApp()
    print("dir:", m.selectedDir)