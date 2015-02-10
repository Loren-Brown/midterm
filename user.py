def fun():
	from Tkinter import *

	#Term Window
	master = Tkinter.Tk()
	e = Entry(master)
	e.pack()

	e.focus_set()

	def callback():
		print e.get() # This is the text you may want to use later

	b = Button(master, text = "OK", width = 10, command = callback)
	b.pack()

if __name__ == '__main__':
	# test1.py executed as script
	# do something
	fun()