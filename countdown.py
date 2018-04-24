#!/usr/bin/python
import sys
#for mac running python3
#import Tkinter as TK
#from Tkinter import *

#for the pi running python3
import Tkinter as TK
from Tkinter import *
import time

#window stuff
window = TK.Tk()
window.title('countdown timer')
window.geometry("100x100")


def countdown(i):
	clock['text'] = i

	if i > 0:
		#run again after 1000 ms/1s
		window.after(1000, countdown, i - 1)
	else:
		clock['text'] = 'DONE'

def run():
	# countdown(timeLeft)
	count = IntVar()
	count = timeLeft.get()
	countdown(int(count))


# timeLeft= int(input("HOW LONG?"))
timeLeft = Entry(window)
timeLeft.pack()
timeLeft.focus_set()

clock = TK.Label(window, bg='red')
clock.place(x = 55, y = 55)

done = Button(window, text='done', command=run)
done.pack(side='bottom')


window.mainloop()



