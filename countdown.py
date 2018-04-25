#TODO:
#other buttons (for actual stops)
#keyboard (numbers)
#add in possibility of DECISECOND

#!/usr/bin/python
import sys
#for mac running python3
import tkinter as TK
from tkinter import *

#for the pi running python3
# import Tkinter as TK
# from Tkinter import *

global isRunning
global reset_it
global stopValues
stopValues = {}
global stop
stop = {}

isRunning = False
reset_it = False


################### WINDOW SETUP ##########################   
window = TK.Tk()
window.title('countdown timer')
window.geometry("500x300")

mainFrame = Frame(window)
mainFrame.pack()

topFrame = Frame(window)
topFrame.pack()

bottomFrame = Frame(window)
bottomFrame.pack()
################### WINDOW SETUP ##########################   

################### FUNCTIONAL METHODS ##########################   
def countdown(i):
	global isRunning
	global reset_it
	
	if isRunning and reset_it == False:
		timeLeft['state'] = 'disabled'
		clock['text'] = i
		if i > 0:
			#run again after 1000 ms/1s
			window.after(1000, countdown, i - 1)
		else:
			timeLeft['state'] = 'normal'
			print('done')
			clock['text'] = '0'
			done['text'] = 'START'
			isRunning = False

def run():
	global isRunning
	global reset_it

	if reset_it:
		timeLeft['state'] = 'normal'
		count = IntVar()
		count= timeLeft.get()
		clock['text'] = count
		isRunning = False
		done['text'] = 'START'
		reset_it = False

	else:	
		if isRunning:
			timeLeft['state'] = 'normal'
			done['text'] = 'CONTINUE'
			#stop timer
			isRunning = False
		else:
			if done['text'] == 'CONTINUE':
				count = clock['text']
			else:
				count = IntVar()
				count = int(clock['text'])

			done['text'] = 'STOP'
			isRunning = True
			countdown(int(count))

def reset():
	global reset_it
	reset_it = True
	run()

def up(val):
    global stopValues
    global isRunning

    if isRunning == False:
    	stopValues[val] +=1
    	updateTextButton(val)

def down(val):
    global stopValues
    global isRunning

    if isRunning == False:
    	if int(stopValues[val]) > 0:
    		stopValues[val] -=1
    		updateTextButton(val)
################### FUNCTIONAL METHODS ##########################   

################### UPDATE METHODS ##########################   
def updatetext(event):
    clock['text'] = int(timeLeft.get()) + int(sum(stopValues.values()))
    window.update_idletasks()  

def updateTextButton(val):
    stop[val]['text'] = stopValues[val]
    clock['text'] = int(timeLeft.get()) + int(sum(stopValues.values()))
    window.update_idletasks()
################### UPDATE METHODS ##########################   


################### FUNCTIONAL BUTTONS ##########################
timeLeft = Entry(mainFrame)
timeLeft.grid(row=0,column=7, ipadx = 10)
timeLeft.focus_set()
timeLeft.config(width=4)
timeLeft.bind(sequence='<KeyRelease>', func=updatetext)

clock = TK.Label(bottomFrame, font = (None,45), text=timeLeft.get())
clock.pack()

done = Button(bottomFrame, text='START', command=run)
done.pack()

reset = Button(bottomFrame, text='RESET', command=reset)
reset.pack()
################### FUNCTIONAL BUTTONS ##########################


################### F/STOP BUTTONS ##########################
stopValues[0] = 0
stop[0] = TK.Label(topFrame, font=(None, 15), text = stopValues[0])
stop[0].grid(row=1,column=3)

addButton0 = Button(topFrame, text='+', command=lambda: up(0))
addButton0.grid(row=5,column=4)

subButton0 = Button(topFrame, text='-', command=lambda: down(0))
subButton0.grid(row=5,column=2)

stopValues[1] = 0
stop[1] = TK.Label(topFrame, font=(None, 15), text = stopValues[1])
stop[1].grid(row=1,column=7)

addButton1 = Button(topFrame, text='+', command=lambda: up(1))
addButton1.grid(row=5,column=8)

subButton1 = Button(topFrame, text='-', command=lambda: down(1))
subButton1.grid(row=5,column=6)

stopValues[2] = 0
stop[2] = TK.Label(topFrame, font=(None, 15), text = stopValues[2])
stop[2].grid(row=1,column=11)

addButton2 = Button(topFrame, text='+', command=lambda: up(2))
addButton2.grid(row=5,column=12)

subButton2 = Button(topFrame, text='-', command=lambda: down(2))
subButton2.grid(row=5,column=10)
################### F/STOP BUTTONS ##########################


window.mainloop()



