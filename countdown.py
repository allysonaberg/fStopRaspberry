#TODO:
#reset button functionality
#other buttons (for actual stops)
#keyboard (numbers)

#!/usr/bin/python
import sys
#for mac running python3
import tkinter as TK
from tkinter import *

#for the pi running python3
# import Tkinter as TK
# from Tkinter import *

#window stuff
window = TK.Tk()
window.title('countdown timer')
window.geometry("500x200")

mainFrame = Frame(window)
mainFrame.pack(expand=True)

global isRunning
global reset_it

isRunning = False
reset_it = False

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
			done['text'] = '...'
			#stop timer
			isRunning = False
		else:
			if done['text'] == '...':
				count = clock['text']
			else:
				count = IntVar()
				count = timeLeft.get()

			done['text'] = 'STOP'
			isRunning = True
			countdown(int(count))

def reset():
	global reset_it
	reset_it = True
	run()

def updatetext(event):
    clock['text'] = timeLeft.get()
    print(timeLeft.get())
    window.update_idletasks()  

timeLeft = Entry(mainFrame)
timeLeft.pack()
timeLeft.focus_set()
timeLeft.config(width=3)
timeLeft.bind(sequence='<KeyRelease>', func=updatetext)


clock = TK.Label(mainFrame, font = (None,30), text=timeLeft.get())
clock.pack()

done = Button(mainFrame, text='START', command=run)
done.pack()


reset = Button(mainFrame, text='RESET', command=reset)
reset.pack()

window.mainloop()



