#TODO:
#get proper stop numbers in
#keyboard (numbers)

#!/usr/bin/python
import sys
#for mac running python3
# import tkinter as TK
# from tkinter import *

#for the pi running python3
import Tkinter as TK
from Tkinter import *

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
window.attributes("-fullscreen", True)

mainFrame = Frame(window)
# mainFrame.pack(padx=0,pady=80)

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
		baseSeconds['state'] = 'disabled'
		baseDeciseconds['state'] = 'disabled'

		clock['text'] = str(sec) + "." + str(deci)

		if deci > 0:
			window.after(100, countdown, sec, deci - 1)
		elif sec > 0 and deci == 0:
			window.after(100, countdown, sec - 1, 9)
		else:
			baseSeconds['state'] = 'normal'
			baseDeciseconds['state'] = 'normal'
			print('done')
			clock['text'] = '0.0'
			done['text'] = 'START'
			isRunning = False

def run():
	global isRunning
	global reset_it

	#RESET CASE
	if reset_it:
		baseSeconds['state'] = 'normal'
		baseDeciseconds['state'] = 'normal'
		count = IntVar()
		count= str(baseSeconds.get()) + '.' + str(baseDeciseconds.get())
		clock['text'] = count
		isRunning = False
		done['text'] = 'START'
		reset_it = False

	#OTHER RUNNING OPERATIONS
	else:	
		#PAUSED
		if isRunning:
			baseSeconds['state'] = 'normal'
			baseDeciseconds['state'] = 'normal'
			done['text'] = 'CONTINUE'
			#stop timer
			isRunning = False

		#START/CONTINUE
		else:
			if done['text'] == 'CONTINUE':
				count = str(clock['text'])
			else:
				count = str(clock['text'])

			done['text'] = 'STOP'
			isRunning = True
			#TODO: MAKE THIS PARSE SMARTER
			sec = int(count.split('.')[0])
			deci = int(count.split('.')[1])
			print(deci)
			countdown(sec, deci)

def reset():
	global reset_it
	global stopValues

	for key in stopValues:
		stopValues[key] = 0
		updateTextButton(key)

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
    clock['text'] = float(baseSeconds.get()) + float( "." + str(baseDeciseconds.get())) + int(sum(stopValues.values()))
    window.update_idletasks()  

def updateTextButton(val):
    stop[val]['text'] = stopValues[val]
    clock['text'] = float(baseSeconds.get()) + float("." +baseDeciseconds.get()) + int(sum(stopValues.values()))
    window.update_idletasks()
################### UPDATE METHODS ##########################   


################### FUNCTIONAL BUTTONS ##########################
baseSeconds = Entry(mainFrame)
baseSeconds.grid(row=0,column=7)
baseSeconds.focus_set()
baseSeconds.config(width=2, font = (None, 55))
baseSeconds.bind(sequence='<KeyRelease>', func=updatetext)
baseSeconds.insert(0, '0')

baseDeciseconds = Entry(mainFrame)
baseDeciseconds.grid(row=0,column=10)
baseDeciseconds.focus_set()
baseDeciseconds.config(width=1, font = (None, 55))
baseDeciseconds.bind(sequence='<KeyRelease>', func=updatetext)
baseDeciseconds.insert(0, '0')

print(baseDeciseconds.get())
clock = TK.Label(bottomFrame, font = (None,100), text=baseSeconds.get() + baseDeciseconds.get())
clock.pack()

done = Button(bottomFrame, text='START', command=run, font = (None, 35))
done.pack()

reset = Button(bottomFrame, text='RESET', command=reset, font = (None, 35))
reset.pack()
################### FUNCTIONAL BUTTONS ##########################


################### F/STOP BUTTONS ##########################
stopValues[0] = 0
stop[0] = TK.Label(topFrame, font=(None, 25), text = stopValues[0])
stop[0].grid(row=1,column=3)

addButton0 = Button(topFrame, text='+', command=lambda: up(0), font = (None, 25))
addButton0.grid(row=5,column=4)

subButton0 = Button(topFrame, text='-', command=lambda: down(0), font = (None, 25))
subButton0.grid(row=5,column=2)

stopValues[1] = 0
stop[1] = TK.Label(topFrame, font=(None, 35), text = stopValues[1])
stop[1].grid(row=1,column=7)

addButton1 = Button(topFrame, text='+', command=lambda: up(1), font = (None, 25))
addButton1.grid(row=5,column=8)

subButton1 = Button(topFrame, text='-', command=lambda: down(1), font = (None, 25))
subButton1.grid(row=5,column=6)

stopValues[2] = 0
stop[2] = TK.Label(topFrame, font=(None, 35), text = stopValues[2])
stop[2].grid(row=1,column=11)

addButton2 = Button(topFrame, text='+', command=lambda: up(2), font = (None, 25))
addButton2.grid(row=5,column=12)

subButton2 = Button(topFrame, text='-', command=lambda: down(2),font = (None, 25))
subButton2.grid(row=5,column=10)
################### F/STOP BUTTONS ##########################


window.mainloop()



