from tkinter import *
import mainmenu

canvasWidth = 1000
canvasHeight = 700

window = Tk()
window.title("main menu")
canvas = Canvas(window, width=canvasWidth, height=canvasHeight)
canvas.config(bg="black")
canvas.pack()

class PauseMenu():
    def __init__(self):
        self.menuSelect = 1
        self.mainRunning = True
    def pauseMenu(self):
        if self.mainRunning:
            canvas.delete(ALL)
            if self.menuSelect == 1:
                canvas.create_rectangle(325, 250, 700, 300, fill="white")
            if self.menuSelect == 2:
                canvas.create_rectangle(325, 350, 700, 400, fill="white")
            if self.menuSelect == 3:
                canvas.create_rectangle(325, 450, 700, 500, fill="white")
            canvas.create_text(510, 275, text="Resume", font=(None, 25), fill="red")
            canvas.create_text(510, 375, text="Restart", font=(None, 25), fill="red")
            canvas.create_text(510, 475, text="Main Menu", font=(None, 25), fill="red")
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
