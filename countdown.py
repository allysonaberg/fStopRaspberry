#TODO:
#reset button functionality
#other buttons (for actual stops)
#keyboard (numbers)

#!/usr/bin/python
import sys
#for mac running python3
# import tkinter as TK
# from tkinter import *

#for the pi running python3
import Tkinter as TK
from Tkinter import *

#window stuff
window = TK.Tk()
window.title('countdown timer')
window.geometry("500x200")

mainFrame = Frame(window)
mainFrame.pack(expand=True)

global isRunning

isRunning = False

def countdown(i):
	global isRunning
	if isRunning:
		clock['text'] = i
		if i > 0:
			#run again after 1000 ms/1s
			window.after(1000, countdown, i - 1)
		else:
			print('done')
			clock['text'] = '0'
			done['text'] = 'START'
			isRunning = False

def run():
	global isRunning

	continue_count = False

	if isRunning:
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


timeLeft = Entry(mainFrame)
timeLeft.pack()
timeLeft.focus_set()
timeLeft.config(width=3)

clock = TK.Label(mainFrame, font = (None,26), text='0')
clock.pack()

done = Button(mainFrame, text='START', command=run)
done.pack()


reset = Button(mainFrame, text='RESET')
reset.pack()

window.mainloop()



