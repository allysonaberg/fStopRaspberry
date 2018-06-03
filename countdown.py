import sys
#for mac running python3
# import tkinter as tk
# from tkinter import *


#for the pi running python2
import Tkinter as tk
from Tkinter import *

LARGE_FONT= ("Verdana", 12)
LARGER_FONT = ("Verdana", 20)

class MainApplication(tk.Tk): #main class inheriting everything from tk.TK
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #initializing the inherited class

        self.geometry("800x480")
        self.configure(background='black')
        self.resizable(0,0)
        self.wm_attributes('-fullscreen','true')

        #defining the container that will hold all our frames:
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0)
        container.configure(background='black')

        self.frames = {}

        frame = StartPage(container, self)
        frame1 = PageOne(container, self)
        frame2 = PageTwo(container, self)

        self.frames[StartPage] = frame
        self.frames[PageOne] = frame1
        # self.frames[PageTwo] = frame2

        frame.grid(row=0, column=0, sticky = "nsew")
        frame1.grid(row=0, column=0, sticky = "nsew")
        frame2.grid(row=0, column=0, sticky = "nsew")

        frame.configure(background="black")
        frame1.configure(background="black")

        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

    def quit(self):
        self.destroy()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        container = tk.Frame(self)
        container.configure(background='black')
        self.configure(background="black")

        button = tk.Button(self, text="F-Stop timer", command=lambda: controller.show_frame(PageOne), font=LARGER_FONT, fg='red', bg='black', compound='center', activebackground='black', activeforeground='red',  highlightthickness=0, borderwidth=0)
        button.grid(row=1, column=0, padx=300, pady = 40)

        # button2 = tk.Button(self, text="Page 2", command=lambda: controller.show_frame(PageTwo), font=LARGER_FONT, fg='red', bg='black', compound='center', activebackground='black', activeforeground='red',  highlightthickness=0, borderwidth=0)
        # button2.grid(row=2, column=0, pady = 20)

        quitButton = tk.Button(self, text="quit", command=lambda: controller.quit(), font=LARGER_FONT, fg='red', bg='black', compound='center', activebackground='black', activeforeground='red',  highlightthickness=0, borderwidth=0)
        quitButton.grid(row=3, column=0)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        controller.configure(background='black')
        tk.Frame.__init__(self, parent)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0)
        container.configure(background='black')

        frame1 = PageOneBlock(container, self)
        frame2 = PageOneBlock(container, self)
        frame1.grid(row=0, column=0, sticky = "nsew")
        frame2.grid(row=1, column=0, sticky = "nsew")

        sideMenuFrame = SideMenu(container, self)
        sideMenuFrame.grid(row=0, column=1, sticky="nsew")

    def show_frame(self, frame):
        self.controller.show_frame(frame)

class SideMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.frame = self
        self.frame.configure(background="black")

        self.menu = tk.PhotoImage(file="burn-button.png")

        self.menuButton = Button(self.frame, image=self.menu, bg = 'black',fg = 'red', compound='center', activebackground='black', activeforeground='red', highlightthickness=0, borderwidth=0, command=lambda: controller.show_frame(StartPage))
        self.menuButton.grid(row=1, column=2, padx=20, pady=2)

#TODO: move this all to another file maybe? This file should only deal with general structure
class PageOneBlock(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.topFrame = self
        self.topFrame.configure(background="black")
        self.isRunning = False
        self.reset_it = False
        self.stopValues = {}
        self.stop = {}
        self.baseSeconds = 0
        self.baseDeciseconds = 0
		################### FUNCTIONAL BUTTONS ##########################
        self.clockImage = tk.PhotoImage(file="clock.png")
        self.resetButton = tk.PhotoImage(file="reset-button.png")
        self.dodgeButton = tk.PhotoImage(file="dodge-button.png")
        self.burnButton = tk.PhotoImage(file="burn-button.png")
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
        self.upButton = tk.PhotoImage(file="up-button.png")
        self.downButton = tk.PhotoImage(file="down-button.png")

        self.stopValues[0] = 0
        self.stop[0] = tk.Label(self.topFrame, font=(None, 35), text = 10, fg = 'red', bg = 'black')
        self.stop[0].grid(row=3,column=2, padx=3, pady=2)

        self.addButton0 = Button(self.topFrame, image=self.upButton, command=lambda:self.up(0,10), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.addButton0.grid(row=1,column=2, padx=3, pady=2)

        self.subButton0 = Button(self.topFrame, image=self.downButton, command=lambda:self.down(0,10),highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.subButton0.grid(row=5,column=2, padx=3, pady=2)

        self.stopValues[1] = 0
        self.stop[1] = tk.Label(self.topFrame, font=(None, 35), text = 5, fg = 'red', bg = 'black')
        self.stop[1].grid(row=3,column=7)

        self.addButton1 = Button(self.topFrame, image=self.upButton, command=lambda: self.up(1,5), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.addButton1.grid(row=1,column=7, padx=3, pady=2)

        self.subButton1 = Button(self.topFrame, image=self.downButton, command=lambda: self.down(1,5), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.subButton1.grid(row=5,column=7, padx=3, pady=2)

        self.stopValues[2] = 0
        self.stop[2] = tk.Label(self.topFrame, font=(None, 35), text = 1, fg = 'red', bg = 'black')
        self.stop[2].grid(row=3,column=12, padx=3, pady=2)

        self.addButton2 = Button(self.topFrame, image=self.upButton, command=lambda: self.up(2,1), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.addButton2.grid(row=1,column=12, padx=3, pady=2)

        self.subButton2 = Button(self.topFrame, image=self.downButton, command=lambda: self.down(2,1),font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.subButton2.grid(row=5,column=12, padx=3, pady=2)

        self.stopValues[3] = 0
        self.stop[3] = tk.Label(self.topFrame, font=(None, 35), text = .1, fg = 'red', bg = 'black')
        self.stop[3].grid(row=3,column=17)

        self.addButton3 = Button(self.topFrame, image=self.upButton, command=lambda: self.up(3,1), font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.addButton3.grid(row=1,column=17, padx=3, pady=2)

        self.subButton3 = Button(self.topFrame, image=self.downButton, command=lambda: self.down(3,1),font = (None, 25), highlightthickness=0, borderwidth=0,bg = 'black', activebackground='black', activeforeground='red')
        self.subButton3.grid(row=5,column=17, padx=3, pady=2)
        ################### F/STOP BUTTONS ##########################

    ################### FUNCTIONAL METHODS ##########################
    def countdown(self, sec, deci):
        self.focus()
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
        self.focus()
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
        self.focus()

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
            self.focus()

    def down(self,val, amt):
	    if self.stopValues[val] != 0:
	    	if self.isRunning == False:
	    		self.stopValues[val] -=amt

	    		if val == 3:
	    			self.baseDeciseconds-=amt
	    		else:
	    			self.baseSeconds-=amt
	    		self.updateTextButton(val)
	    self.focus()
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



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()




app=MainApplication()
app.mainloop()
