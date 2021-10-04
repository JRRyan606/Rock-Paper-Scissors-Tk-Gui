from tkinter import *
import random

win = Tk()
win.title("Rock, Paper, Scissors")
win.geometry("801x300")


options = ["rock", "paper", "scissors"]
computer = random.choice(options)



def show():
	info = "Computer choose: " + computer
	info2 = "You choose: " + str(e.get()).lower()
	if str(e.get()).lower() == computer:
		text3 = Label(win, text="ITS A TIE!!", font=('Arial', 18))
		text3.pack()
 
	elif str(e.get()).lower() == "rock":
		if computer == "paper":
			text4 = Label(win, text="The computer wins!, you lose", font=('Arial', 18))
			text4.pack()

		if computer == "scissors":
			text5 = Label(win, text="You win!, the computer lose", font=('Arial', 18))
			text5.pack()

	elif str(e.get()).lower() == "scissors":
		if computer == "rock":
			text6 = Label(win, text="The computer wins!, you lose", font=('Arial', 18))
			text6.pack()

		if computer == "paper":
			text7 = Label(win, text="You win!, the computer lose", font=('Arial', 18))
			text7.pack()

	elif str(e.get()).lower() == "paper":
		if computer == "scissors":
			text8 = Label(win, text="The computer wins!, you lose", font=('Arial', 18))
			text8.pack()

		if computer == "rock":
			text9 = Label(win, text="You win!, the computer lose", font=('Arial', 18))
			text9.pack()

	elif str(e.get()).lower() is not options:
		text10 = Label(win, text="There is no such thing as " + str(e.get()).lower() + " in this game. " + "Please enter the correct word", fg="red", font=('Arial', 18))
		text10.pack()

	text1 = Label(win, text=info, font=('Arial', 18))
	text1.pack()
	text2 = Label(win, text=info2, font=('Arial', 18))
	text2.pack()





lab = Label(win, text="Rock, Paper or Scissors?", font=('Arial', 18))
lab.pack()


e = Entry(win, borderwidth=10, bg="powderblue")
e.pack()


b = Button(win, text="Submit", font=('Arial', 18), bg="lightgreen", command=show)
b.pack()
win.mainloop()
