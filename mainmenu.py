from tkinter import *

canvasWidth = 1000
canvasHeight = 700

window = Tk()
window.title("main menu")
canvas = Canvas(window, width=canvasWidth, height=canvasHeight)
canvas.config(bg="black")
canvas.pack()

leftArrow = PhotoImage(file="arrowleft.gif")
rightArrow = PhotoImage(file="arrowright.gif")
backgroundImage = PhotoImage(file="background.gif")

class MainMenu():
    def __init__(self):
        self.menuSelect = 1
        self.mainRunning = True

    def mainMenu(self):
        #in an if statement because keeps
        #putting menu on screen otherwise
        if self.mainRunning:
            canvas.delete(ALL)
            canvas.create_image(375, 250, image=backgroundImage)
            if self.menuSelect == 1:
                canvas.create_image(600, 225, image=leftArrow)
                canvas.create_image(415, 225, image=rightArrow)
            if self.menuSelect == 2:
                canvas.create_image(635, 325, image=leftArrow)
                canvas.create_image(375, 325, image=rightArrow)
            if self.menuSelect == 3:
                canvas.create_image(600, 425, image=leftArrow)
                canvas.create_image(415, 425, image=rightArrow)
            canvas.create_text(510, 225, text="Play", font=("Space Bd BT", 35), fill="red")
            canvas.create_text(510, 325, text="Settings", font=("Space Bd BT", 35), fill="red")
            canvas.create_text(510, 425, text="Quit", font=("Space Bd BT", 35), fill="red")
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
