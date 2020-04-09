from tkinter import *

class Invalid_Popup:

	def __init__(self):
		invalid = Tk()
		invalid.title('Invalid')
		invalid.geometry('250x100')

		frame_invalid = Frame(invalid)
		frame_invalid.pack(fill=BOTH, expand = True)

		self.data_label = Label(frame_invalid, text = 'You did not enter all inputs properly...')
		self.data_label.place(x = 20, y = 20)

		cancel = Button(frame_invalid, text = 'CANCEL', width = 10, bg = '#fc4445', command = invalid.destroy)
		cancel.place(x = 85, y = 55)