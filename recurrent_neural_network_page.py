from tkinter import *

class Recurrent_Neural_Net_Page:

	def __init__(self):
		nn_window = Tk()
		nn_window.title('Neural Network')
		nn_window.configure(bg = '#abb1b3')
		nn_window.geometry('1000x500')

		frame_2 = Frame(nn_window)
		frame_2.pack(fill=BOTH, expand = True)

		self.data_label = Label(frame_2, text = 'Still in progress...', width = 20, bd = 2, relief = 'solid', anchor=CENTER)
		self.data_label.place(x = 30, y = 20)