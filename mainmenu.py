from tkinter import *
import pausemenu

canvasWidth = 1000
canvasHeight = 700

window = Tk()
window.title("main menu")
canvas = Canvas(window, width=canvasWidth, height=canvasHeight)
canvas.config(bg="black")
canvas.pack()

class MainMenu():
    def __init__(self):
        self.menuSelect = 1
        self.mainRunning = True
    def mainMenu(self):
        #in an if statement because keeps
        #putting menu on screen otherwise
        if self.mainRunning:
            canvas.delete(ALL)
            if self.menuSelect == 1:
                canvas.create_rectangle(325, 250, 700, 300, fill="white")
            if self.menuSelect == 2:
                canvas.create_rectangle(325, 350, 700, 400, fill="white")
            if self.menuSelect == 3:
                canvas.create_rectangle(325, 450, 700, 500, fill="white")
            canvas.create_text(510, 275, text="Play", font=(None, 25), fill="red")
            canvas.create_text(510, 375, text="Settings", font=(None, 25), fill="red")
            canvas.create_text(510, 475, text="Quit", font=(None, 25), fill="red")
            window.after(16, self.mainMenu)

    def menuDown(self, event):
        if self.menuSelect <= 3:
            self.menuSelect += 1
        else:
            self.menuSelect = 1

    def menuUp(self, event):
        if self.menuSelect >= 0:
            self.menuSelect -= 1
        else:
            self.menuSelect = 3

    def startGame(self):
        self.mainRunning = False
        canvas.delete(ALL)
        print("game start")

    def openSettings(self):
        print("settings")

    def enterPressed(self, event):
        if self.menuSelect == 1:
            self.startGame()
        if self.menuSelect == 2:
            self.openSettings()
        if self.menuSelect == 3:
            window.destroy()

menu = MainMenu()
menu.mainMenu()

window.bind("<Up>", menu.menuUp)
window.bind("<Down>", menu.menuDown)
window.bind("<Return>", menu.enterPressed)

window.mainloop()
