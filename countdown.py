#TODO:
#get proper stop numbers in
#keyboard (numbers)
#
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
global baseSeconds
global baseDeciseconds

stopValues = {}
global stop
stop = {}

baseSeconds = 0
baseDeciseconds = 0
isRunning = False
reset_it = False


################### WINDOW SETUP ##########################   
window = TK.Tk()
window.title('countdown timer')
window.geometry("800x450")

mainFrame = Frame(window)
mainFrame.pack()

topFrame = Frame(window)
topFrame.pack()

bottomFrame = Frame(window)
bottomFrame.pack()
################### WINDOW SETUP ##########################   

################### FUNCTIONAL METHODS ##########################   
def countdown(sec, deci):
	global isRunning
	global reset_it
	
	if isRunning and reset_it == False:
		clock['text'] = str(sec) + "." + str(deci)

		if deci > 0:
			window.after(100, countdown, sec, deci - 1)
		elif sec > 0 and deci == 0:
			window.after(100, countdown, sec - 1, 9)
		else:
			print('done')
			clock['text'] = '0.0'
			isRunning = False

def run():
	global isRunning
	global reset_it

	#RESET CASE
	if reset_it:
		count = IntVar()
		count= str(baseSeconds) + '.' + str(baseDeciseconds)
		clock['text'] = count
		isRunning = False
		reset_it = False

	#OTHER RUNNING OPERATIONS
	else:	
		#PAUSED
		if isRunning:
			isRunning = False

		#START/CONTINUE
		else:
			count = str(clock['text'])
			isRunning = True

			#TODO: MAKE THIS PARSE SMARTER
			sec = int(count.split('.')[0])
			deci = int(count.split('.')[1])
			countdown(sec, deci)

def reset():
	global reset_it
	global stopValues

	for key in stopValues:
		stopValues[key] = 0
		updateTextButton(key)

	reset_it = True
	run()

def up(val, amt):
    global stopValues
    global isRunning
    global baseSeconds
    global baseDeciseconds

    if isRunning == False:
    	stopValues[val] +=amt

    	if val == 3:
    		baseDeciseconds+=amt
    	else:
    		baseSeconds+=amt
    	updateTextButton(val)

def down(val, amt):
    global stopValues
    global isRunning
    global baseSeconds
    global baseDeciseconds

    if stopValues[val] != 0:
    	if isRunning == False:
    		stopValues[val] -=amt

    		if val == 3:
    			baseDeciseconds-=amt
    		else:
    			baseSeconds-=amt
    		updateTextButton(val)
################### FUNCTIONAL METHODS ##########################   

################### UPDATE METHODS ##########################   
def updatetext(event):
    clock['text'] = str(baseSeconds) + "." + str(baseDeciseconds)
    window.update_idletasks()  

def updateTextButton(val):
    stop[val]['text'] = stopValues[val]
    clock['text'] = str(baseSeconds) + "." + str(baseDeciseconds)
    window.update_idletasks()
################### UPDATE METHODS ##########################   


################### FUNCTIONAL BUTTONS ##########################
clock = Button(bottomFrame, font = (None,100), text=baseSeconds + baseDeciseconds, command=run)
clock.grid(row=3,column=10)

################### FUNCTIONAL BUTTONS ##########################


################### F/STOP BUTTONS ##########################
stopValues[0] = 0
stop[0] = TK.Label(topFrame, font=(None, 35), text = stopValues[0])
stop[0].grid(row=1,column=3)

addButton0 = Button(topFrame, text='+', command=lambda: up(0,10), font = (None, 25))
addButton0.grid(row=5,column=4)

subButton0 = Button(topFrame, text='-', command=lambda: down(0,10), font = (None, 25))
subButton0.grid(row=5,column=2)

stopValues[1] = 0
stop[1] = TK.Label(topFrame, font=(None, 35), text = stopValues[1])
stop[1].grid(row=1,column=7) 

addButton1 = Button(topFrame, text='+', command=lambda: up(1,5), font = (None, 25))
addButton1.grid(row=5,column=8)

subButton1 = Button(topFrame, text='-', command=lambda: down(1,5), font = (None, 25))
subButton1.grid(row=5,column=6)

stopValues[2] = 0
stop[2] = TK.Label(topFrame, font=(None, 35), text = stopValues[2])
stop[2].grid(row=1,column=11)

addButton2 = Button(topFrame, text='+', command=lambda: up(2,1), font = (None, 25))
addButton2.grid(row=5,column=12)

subButton2 = Button(topFrame, text='-', command=lambda: down(2,1),font = (None, 25))
subButton2.grid(row=5,column=10)

stopValues[3] = 0
stop[3] = TK.Label(topFrame, font=(None, 35), text = stopValues[3])
stop[3].grid(row=1,column=15)

addButton3 = Button(topFrame, text='+', command=lambda: up(3,1), font = (None, 25))
addButton3.grid(row=5,column=16)

subButton3 = Button(topFrame, text='-', command=lambda: down(3,1),font = (None, 25))
subButton3.grid(row=5,column=14)
################### F/STOP BUTTONS ##########################


window.mainloop()



