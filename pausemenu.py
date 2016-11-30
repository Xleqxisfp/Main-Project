from tkinter import *

canvasWidth = 1000
canvasHeight = 700

window = Tk()
window.title("pause menu")
canvas = Canvas(window, width=canvasWidth, height=canvasHeight)
canvas.config(bg="black")
canvas.pack()

leftArrow = PhotoImage(file="arrowleft.gif")
rightArrow = PhotoImage(file="arrowright.gif")
backgroundImage = PhotoImage(file="background.gif")

class PauseMenu():
    def __init__(self):
        self.menuSelect = 1
        self.mainRunning = True
    def pauseMenu(self):
        if self.mainRunning:
            canvas.delete(ALL)
            canvas.create_image(375, 250, image=backgroundImage)
            if self.menuSelect == 1:
                canvas.create_image(615, 250, image=leftArrow)
                canvas.create_image(400, 250, image=rightArrow)
            if self.menuSelect == 2:
                canvas.create_image(600, 350, image=leftArrow)
                canvas.create_image(415, 350, image=rightArrow)
            if self.menuSelect == 3:
                canvas.create_image(630, 450, image=leftArrow)
                canvas.create_image(390, 450, image=rightArrow)
            canvas.create_text(510, 250, text="Resume", font=("Space Bd BT", 25), fill="red")
            canvas.create_text(510, 350, text="Restart", font=("Space Bd BT", 25), fill="red")
            canvas.create_text(510, 450, text="Main Menu", font=("Space Bd BT", 25), fill="red")
            window.after(16, self.pauseMenu)

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

    def resumeGame(self):
        print("resume game")

    def restartGame(self):
        print("restart game")

    def exitToMenu(self):
        self.mainRunning = False
        canvas.delete(ALL)
        print("exit to menu")

    def enterPressed(self, event):
        if self.menuSelect == 1:
            self.resumeGame()
        if self.menuSelect == 2:
            self.restartGame()
        if self.menuSelect == 3:
            self.exitToMenu()

menu = PauseMenu()
menu.pauseMenu()

window.bind("<Up>", menu.menuUp)
window.bind("<Down>", menu.menuDown)
window.bind("<Return>", menu.enterPressed)

window.mainloop()
