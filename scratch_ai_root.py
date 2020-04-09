from tkinter import *
from recurrent_neural_network_page import *
from tkinter.ttk import *
from neural_network_page import *
from PIL import Image, ImageTk

class Buttons:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack(fill=BOTH, expand = True)

		myFont = font.Font(family='Helvetica')

		self.neural_net_button = Button(frame, text = 'Neural Network - Image Classification', bg = '#5de8df', command = self.create_neural_net)
		self.neural_net_button['font'] = myFont
		self.neural_net_button.pack(side = LEFT, fill = BOTH, expand = True)

		self.recurrent_neural_net_button = Button(frame, text = 'Recurrent Neural Network - Time Series', bg = '#5de8df', command = self.create_recurrent_neural_net)
		self.recurrent_neural_net_button['font'] = myFont
		self.recurrent_neural_net_button.pack(side = LEFT, fill = BOTH, expand = True)

	def create_neural_net(self):
		nn_page = Neural_Net_Page()

	def create_recurrent_neural_net(self):
		rnn_page = Recurrent_Neural_Net_Page()
		

root = Tk()
root.title('AI/O - Beta Edition 1.01')
root.configure(bg = '#ffffff')
root.geometry('1000x500')

logo = ImageTk.PhotoImage(Image.open('AI_dash_O_logo.png'))
ai_logo = Label(root, image = logo, bd = 0)
ai_logo.pack()

b = Buttons(master = root)
root.mainloop()