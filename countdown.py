#TODO:
#other buttons (for actual stops)
#keyboard (numbers)
#does it have miliseconds?

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
global testStopValue
testStopValue = 0
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
				count = int(timeLeft.get()) + int(testStopValue)

			done['text'] = 'STOP'
			isRunning = True
			countdown(int(count))

def reset():
	global reset_it
	reset_it = True
	run()

def up(val):
    global testStopValue
    testStopValue +=1
    updateTextButton()

def down(val):
    global testStopValue
    if int(testStopValue) > 0:
    	testStopValue -=1
    	updateTextButton()
################### FUNCTIONAL METHODS ##########################   

################### UPDATE METHODS ##########################   
def updatetext(event):
    clock['text'] = int(timeLeft.get()) + int(testStopValue)
    window.update_idletasks()  

def updateTextButton():
    testStop['text'] = testStopValue
    clock['text'] = int(timeLeft.get()) + int(testStopValue)
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
testStopValue = 0
testStop = TK.Label(topFrame, font=(None, 15), text = testStopValue)
testStop.grid(row=1,column=3)

testAddButton = Button(topFrame, text='+', command=up)
testAddButton.grid(row=5,column=4)

testSubButton = Button(topFrame, text='-', command=down)
testSubButton.grid(row=5,column=2)

testStopValue1 = 0
testStop = TK.Label(topFrame, font=(None, 15), text = testStopValue1)
testStop.grid(row=1,column=7)

testAddButton1 = Button(topFrame, text='+', command=up)
testAddButton1.grid(row=5,column=8)

testSubButton1 = Button(topFrame, text='-', command=down)
testSubButton1.grid(row=5,column=6)

testStopValue2 = 0
testStop = TK.Label(topFrame, font=(None, 15), text = testStopValue2)
testStop.grid(row=1,column=11)

testAddButton2 = Button(topFrame, text='+', command=up)
testAddButton2.grid(row=5,column=12)

testSubButton2 = Button(topFrame, text='-', command=down)
testSubButton2.grid(row=5,column=10)
################### F/STOP BUTTONS ##########################


window.mainloop()



