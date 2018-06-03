#TODO:
#BOTTOM FRAME W/ REUSABLE CODE (put it in a class or something)
#keyboard (numbers)

#
#!/usr/bin/python
import sys
#for mac running python3
import tkinter as TK
from tkinter import *


#for the pi running python2
# import Tkinter as TK
# from Tkinter import *



################### WINDOW SETUP ##########################
window = TK.Tk()
window.geometry("800x480")
window.configure(background='black')
window.resizable(0,0)
window.wm_attributes('-fullscreen','true')
frame1 = Frame(window)
frame1.grid(row=0,column=0, pady=5)
frame2 = Frame(window)
frame2.grid(row=10,column=0)
menuFrame = Frame(window)
menuFrame.grid(row=0, column=10, padx=40)
################### WINDOW SETUP ##########################

####################### Side Menu #############################
class MainMenu:
	def __init__(self, window, root):
		self.frame = window
		self.frame.configure(background='black')
		self.resetButton = TK.PhotoImage(file="reset-button.png")
		self.mainMenu = Button(self.frame, image=self.resetButton, command=lambda: self.showMenu(self.frame), bg = 'black',fg = 'red', compound='center', activebackground='black', activeforeground='red', highlightthickness=0, borderwidth=0)
		self.mainMenu.grid(row=0, column=60)

		self.quitButton = TK.PhotoImage(file="reset-button.png")
		self.mainMenu = Button(self.frame, image=self.quitButton, command=lambda: self.quit(root), bg = 'black',fg = 'red', compound='center', activebackground='black', activeforeground='red', highlightthickness=0, borderwidth=0)
		self.mainMenu.grid(row=5, column=100)

	############# MENU FXNS #######################
	def showMenu(self, frame):
		self.newWindow = TK.Toplevel(frame)
		self.newWindow.wm_attributes('-fullscreen','true')
		self.newWindow.geometry("800x480")
		self.newWindow.configure(background='black')
		self.app = Menu(self.newWindow)

	def quit(self, root):
		root.destroy()

####################### Main Menu #############################

class page1:

	def __init__(self, window):
		self.topFrame = window
		self.root_color = "black"
		self.topFrame.configure(background=self.root_color)
		self.isRunning = False
		self.reset_it = False
		self.stopValues = {}
		self.stop = {}
		self.baseSeconds = 0
		self.baseDeciseconds = 0
		################### FUNCTIONAL BUTTONS ##########################
		self.clockImage = TK.PhotoImage(file="clock.png")
		self.resetButton = TK.PhotoImage(file="reset-button.png")
		self.dodgeButton = TK.PhotoImage(file="dodge-button.png")
		self.burnButton = TK.PhotoImage(file="burn-button.png")
		self.clock = Button(self.topFrame, image=self.clockImage, font = (None,45), text="000.0", command=self.run, bg = 'black',fg = 'red', compound='center', activebackground='black', activeforeground='red', highlightthickness=0, borderwidth=0)
		self.clock.grid(row=1,column=20, columnspan=6, rowspan=6, padx=5, pady=5)

		self.menu1 = Button(self.topFrame, image=self.resetButton, bg = 'black',fg = 'red', compound='center', command=self.reset, activebackground='black', activeforeground='red', highlightthickness=0, borderwidth=0)
		self.menu1.grid(row=1, column=35)

		self.menu2 = Button(self.topFrame, image=self.dodgeButton, bg = 'black',fg = 'red', compound='center', activebackground='black', activeforeground='red', highlightthickness=0, borderwidth=0)
		self.menu2.grid(row=3, column=35)

		self.menu3 = Button(self.topFrame, image=self.burnButton, bg = 'black',fg = 'red', compound='center', activebackground='black', activeforeground='red', highlightthickness=0, borderwidth=0)
		self.menu3.grid(row=5, column=35)
		################### FUNCTIONAL BUTTONS ##########################


		################### F/STOP BUTTONS  ##########################
		self.upButton = TK.PhotoImage(file="up-button.png")
		self.downButton = TK.PhotoImage(file="down-button.png")

		self.stopValues[0] = 0
		self.stop[0] = TK.Label(self.topFrame, font=(None, 35), text = 10, fg = 'red', bg = 'black')
		self.stop[0].grid(row=3,column=2, padx=3, pady=3)

		self.addButton0 = Button(self.topFrame, image=self.upButton, command=lambda:self.up(0,10), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.addButton0.grid(row=1,column=2, padx=3, pady=3)

		self.subButton0 = Button(self.topFrame, image=self.downButton, command=lambda:self.down(0,10),highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.subButton0.grid(row=5,column=2, padx=3, pady=3)

		self.stopValues[1] = 0
		self.stop[1] = TK.Label(self.topFrame, font=(None, 35), text = 5, fg = 'red', bg = 'black')
		self.stop[1].grid(row=3,column=7)

		self.addButton1 = Button(self.topFrame, image=self.upButton, command=lambda: self.up(1,5), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.addButton1.grid(row=1,column=7, padx=3, pady=3)

		self.subButton1 = Button(self.topFrame, image=self.downButton, command=lambda: self.down(1,5), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.subButton1.grid(row=5,column=7, padx=3, pady=3)

		self.stopValues[2] = 0
		self.stop[2] = TK.Label(self.topFrame, font=(None, 35), text = 1, fg = 'red', bg = 'black')
		self.stop[2].grid(row=3,column=12, padx=3, pady=3)

		self.addButton2 = Button(self.topFrame, image=self.upButton, command=lambda: self.up(2,1), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.addButton2.grid(row=1,column=12, padx=3, pady=3)

		self.subButton2 = Button(self.topFrame, image=self.downButton, command=lambda: self.down(2,1),font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.subButton2.grid(row=5,column=12, padx=3, pady=3)

		self.stopValues[3] = 0
		self.stop[3] = TK.Label(self.topFrame, font=(None, 35), text = .1, fg = 'red', bg = 'black')
		self.stop[3].grid(row=3,column=17)

		self.addButton3 = Button(self.topFrame, image=self.upButton, command=lambda: self.up(3,1), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.addButton3.grid(row=1,column=17, padx=3, pady=3)

		self.subButton3 = Button(self.topFrame, image=self.downButton, command=lambda: self.down(3,1),font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
		self.subButton3.grid(row=5,column=17, padx=3, pady=3)
		################### F/STOP BUTTONS ##########################

	################### FUNCTIONAL METHODS ##########################
	def countdown(self, sec, deci):
		window.focus()
		if self.isRunning and self.reset_it == False:
			self.clock['text'] = str(sec) + "." + str(deci)

			if deci > 0:
				self.topFrame.after(100, self.countdown, sec, deci - 1)
			elif sec > 0 and deci == 0:
				self.topFrame.after(100, self.countdown, sec - 1, 9)
			else:
				print('done')
				self.clock['text'] = '0.0'
				self.isRunning = False

	def run(self):
		window.focus()

		#RESET CASE
		if self.reset_it:
			self.count = IntVar()
			self.count= str(self.baseSeconds) + '.' + str(self.baseDeciseconds)
			self.clock['text'] = self.count
			self.isRunning = False
			self.reset_it = False

		#OTHER RUNNING OPERATIONS
		else:
			#PAUSED
			if self.isRunning:
				self.isRunning = False

			#START/CONTINUE
			else:
				self.count = str(self.clock['text'])
				self.isRunning = True

				#TODO: MAKE THIS PARSE SMARTER
				self.sec = int(self.count.split('.')[0])
				self.deci = int(self.count.split('.')[1])
				self.countdown(self.sec, self.deci)

	def reset(self):
		window.focus()

		for key in self.stopValues:
			self.updateTextButton(key)

		self.reset_it = True
		self.run()

	def up(self,val, amt):
	    if self.isRunning == False:
	    	self.stopValues[val] +=amt

	    	if val == 3:
	    		self.baseDeciseconds+=amt
	    	else:
	    		self.baseSeconds+=amt
	    	self.updateTextButton(val)
	    window.focus()

	def down(self,val, amt):
	    if self.stopValues[val] != 0:
	    	if self.isRunning == False:
	    		self.stopValues[val] -=amt

	    		if val == 3:
	    			self.baseDeciseconds-=amt
	    		else:
	    			self.baseSeconds-=amt
	    		self.updateTextButton(val)
	    window.focus()
	################### FUNCTIONAL METHODS ##########################

	################### UPDATE METHODS ##########################
	def updatetext(self,event):
	    self.clock['text'] = str(self.baseSeconds) + "." + str(self.baseDeciseconds)
	    self.topFrame.update_idletasks()

	def updateTextButton(self,val):
	    # stop[val]['text'] = stopValues[val]
	    self.clock['text'] = str(self.baseSeconds) + "." + str(self.baseDeciseconds)
	    self.topFrame.update_idletasks()
	################### UPDATE METHODS ##########################

MainMenu(menuFrame, window)
page1(frame1)
page1(frame2)
window.mainloop()