from tkinter import *
import tkinter.font as font
from tkinter.ttk import *
from invalid_popup import *

class Neural_Net_Page:

	def __init__(self):

		nn_window = Toplevel()
		nn_window.title('Neural Network')
		nn_window.geometry('1000x600')

		frame = Frame(nn_window)
		frame.pack(fill=BOTH, expand = True)

		self.w = Canvas(frame, width=1000, height=600)
		self.w.pack()

		self.w.create_rectangle(300, 0, 1000, 600, fill="#000000")
		self.w.create_rectangle(0, 0, 300, 200, fill="#545454")
		self.w.create_rectangle(0, 200, 300, 475, fill="#1f2833")
		self.w.create_rectangle(0, 475, 300, 550, fill="#d4d4d4")
		self.w.create_rectangle(300, 400, 1000, 600, fill="#efe2ba")

		myFont = font.Font(family='Helvetica')

		self.dataset_clicked_num = -1

		# layer and label_layers are STACKS
		self.layers = []
		self.label_layers = []
		self.node_circles = []
		self.y_start = 260


		self.data_label = Label(frame, text = 'Datasets', width = 10, anchor=CENTER)
		self.data_label['font'] = myFont
		self.data_label.place(x = 97, y = 20)

		self.mnist = Button(frame, text = 'MNIST', width = 10, bg = '#5de8df', command = lambda: self.dataset_clicked(self.mnist))
		self.mnist['font'] = myFont
		self.mnist.place(x = 95, y = 50)

		self.cifar = Button(frame, text = 'CIFAR-10', width = 10, bg = '#5de8df', command = lambda: self.dataset_clicked(self.cifar))
		self.cifar['font'] = myFont
		self.cifar.place(x = 95, y = 100)

		self.cifar_100 = Button(frame, text = 'CIFAR-100', width = 10, bg = '#5de8df', command = lambda: self.dataset_clicked(self.cifar_100))
		self.cifar_100['font'] = myFont
		self.cifar_100.place(x = 95, y = 150)

		self.layer_label = Label(frame, text = 'Hidden Layers', width = 20, anchor=CENTER)
		self.layer_label['font'] = myFont
		self.layer_label.place(x = 50, y = 220)

		#The label and entry for the nodes in a layer
		layer_label = Label(frame, text = 'Layer 1 Nodes:', anchor=CENTER)
		layer_label.place(x = 40, y = self.y_start)
		self.label_layers.append(layer_label)

		layer = Entry(frame, bg = '#f5a4bb')
		layer.place(x = 125, y = self.y_start+1)
		self.layers.append(layer)

		# Creates a new layer
		self.add_button_image = PhotoImage(file = 'add_layer_button.png')
		self.add_button_image = self.add_button_image.subsample(4, 4) 
		self.add_button = Button(frame, bg = '#03dffc', image = self.add_button_image, border = 0, command = lambda: self.add_new_layer(frame))
		self.add_button.place(x = 105, y = self.y_start+30)

		# Removes current layer
		self.remove_button_image = PhotoImage(file = 'remove_layer_button.png')
		self.remove_button_image = self.remove_button_image.subsample(4, 4)
		self.remove_button = Button(frame, bg = '#f51423', image = self.remove_button_image, border = 0, command = lambda: self.remove_layer(frame), state = DISABLED)
		self.remove_button.place(x = 165, y = self.y_start+30)

		# Creates radio buttons
		self.r = IntVar()

		self.radio_button_time = Radiobutton(frame, text = 'Time', variable = self.r, value = 1, bg = "#d4d4d4", command = lambda: self.radio_clicked(self.r.get()))
		self.radio_button_time.place(x = 45, y = 485)
		self.radio_button_epochs = Radiobutton(frame, text = 'Epochs', variable = self.r, value = 2, bg = "#d4d4d4", command = lambda: self.radio_clicked(self.r.get()))
		self.radio_button_epochs.place(x = 45, y = 515)

		self.time_entry = Entry(frame, bg = '#f5a4bb', state = DISABLED)
		self.time_entry.place(x = 120, y = 490)
		self.epoch_entry = Entry(frame, bg = '#f5a4bb', state = DISABLED)
		self.epoch_entry.place(x = 120, y = 520)

		self.sec_label = Label(frame, text = 'sec', bg = '#d4d4d4')
		self.sec_label.place(x = 250, y = 487)
		self.epoch_label = Label(frame, text = 'epochs', bg = '#d4d4d4')
		self.epoch_label.place(x = 250, y = 517)


		# Creates the defined neural network
		self.create_button_image = PhotoImage(file = 'create_button.png')
		self.create_button_image = self.create_button_image.subsample(3, 3)
		self.create_button = Button(frame, text = 'CREATE', image = self.create_button_image, border = 0,command = lambda: self.create_nn(frame))
		self.create_button.place(x = 100, y = 557)

	def radio_clicked(self, value):
		if(value == 1): # time
			self.time_entry['state'] = NORMAL
			self.epoch_entry['state'] = DISABLED
		elif(value == 2):
			self.time_entry['state'] = DISABLED
			self.epoch_entry['state'] = NORMAL

	def dataset_clicked(self, button):
		button.configure(bg = '#da7b93')

		# self.dataset_clicked_num = -1
		if(self.mnist == button):
			self.dataset_clicked_num = 1
		if(self.cifar == button):
			self.dataset_clicked_num = 2
		if(self.cifar_100 == button):
			self.dataset_clicked_num = 3

		if(self.mnist != button):
			self.mnist.configure(bg = '#5de8df')
		if(self.cifar != button):
			self.cifar.configure(bg = '#5de8df')
		if(self.cifar_100 != button):
			self.cifar_100.configure(bg = '#5de8df')

	def add_new_layer(self, master):

		if(len(self.label_layers) < 6):
			self.y_start = 260

			layer_label = Label(master, text = 'Layer {} Nodes:'.format(len(self.label_layers)+1), anchor=CENTER)
			self.label_layers.append(layer_label)	

			layer = Entry(master, bg = '#f5a4bb')
			self.layers.append(layer)

			for i in self.label_layers:
				i.place(x = 40, y = self.y_start)
				self.y_start = self.y_start + 30
			self.y_start = 260
			for i in self.layers:
				i.place(x = 125, y = self.y_start+1)
				self.y_start = self.y_start + 30

			self.add_button.place(x = 105, y = self.y_start)
			self.remove_button.place(x = 165, y = self.y_start)

			if(len(self.label_layers) == 6):
				self.add_button['state'] = DISABLED
		else:
			self.add_button['state'] = DISABLED

		if(len(self.label_layers) != 0):
			self.remove_button['state'] = NORMAL

	def remove_layer(self, master):

		if(len(self.label_layers) > 1):
			self.label_layers[len(self.label_layers)-1].place_forget()
			self.layers[len(self.layers)-1].place_forget()
			self.label_layers.pop()
			self.layers.pop()

			self.y_start = self.y_start - 30
			self.add_button.place(x = 105, y = self.y_start)
			self.remove_button.place(x = 165, y = self.y_start)

			if(len(self.label_layers) == 1):
				self.remove_button['state'] = DISABLED
		else:
			self.remove_button['state'] = DISABLED

		if(len(self.label_layers) < 8):
			self.add_button['state'] = NORMAL

	# Creates the neural network based on user input
	def create_nn(self, master):

		valid_nn = True

		#check statements make sure everything is correct
		if(self.dataset_clicked_num != -1):
			valid_nn == False
			dataset = self.dataset_clicked_num
			try:

				for i in self.node_circles:
					self.w.delete(i)

				nodes = []
				for i in self.layers:
					nodes.append(int(i.get()))

				if(self.r.get() == 1): # time
					time = int(self.time_entry.get())
				elif(self.r.get() == 2): # epochs
					epochs = int(self.epoch_entry.get())

				'''
				layer fills:
				Layer 0 = #ffffff
				Layer 1 = #d8c385
				Layer 2 = #e85a4f
				Layer 3 = #84ceeb
				Layer 4 = #fff652
				Layer 5 = #86c232
				Layer 6 = #f172a1
				Layer 7 = #f79e02
				'''
				#self.w.create_oval(320, 50, 360, 90, fill = '#f172a1')
				num_layers = len(self.layers)
				start_position_x = 350
				increment = 660/(num_layers+2)

				for i in range(num_layers+1):
					self.create_lines(i, i+1)

				for i in range(num_layers+2):
					if(i == 0):
						self.node_circles.append(self.w.create_oval(start_position_x, 50, start_position_x+40, 90, fill = '#ffffff'))
						self.node_circles.append(self.w.create_oval(start_position_x, 130, start_position_x+40, 170, fill = '#ffffff'))
						self.node_circles.append(self.w.create_oval(start_position_x, 210, start_position_x+40, 250, fill = '#ffffff'))
						self.node_circles.append(self.w.create_oval(start_position_x, 290, start_position_x+40, 330, fill = '#ffffff'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18, 177, start_position_x+23, 182, fill = '#ffffff'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18, 187, start_position_x+23, 192, fill = '#ffffff'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18, 197, start_position_x+23, 202, fill = '#ffffff'))

					if(i == 1):
						self.node_circles.append(self.w.create_oval(start_position_x + (1*increment), 50, start_position_x+40 + (1*increment), 90, fill = '#d8c385'))
						self.node_circles.append(self.w.create_oval(start_position_x + (1*increment), 130, start_position_x+40 + (1*increment), 170, fill = '#d8c385'))
						self.node_circles.append(self.w.create_oval(start_position_x + (1*increment), 210, start_position_x+40 + (1*increment), 250, fill = '#d8c385'))
						self.node_circles.append(self.w.create_oval(start_position_x + (1*increment), 290, start_position_x+40 + (1*increment), 330, fill = '#d8c385'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (1*increment), 177, start_position_x+23+ (1*increment), 182, fill = '#d8c385'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (1*increment), 187, start_position_x+23+ (1*increment), 192, fill = '#d8c385'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (1*increment), 197, start_position_x+23+ (1*increment), 202, fill = '#d8c385'))

					if(i == 2):
						self.node_circles.append(self.w.create_oval(start_position_x + (2*increment), 50, start_position_x+40 + (2*increment), 90, fill = '#e85a4f'))
						self.node_circles.append(self.w.create_oval(start_position_x + (2*increment), 130, start_position_x+40 + (2*increment), 170, fill = '#e85a4f'))
						self.node_circles.append(self.w.create_oval(start_position_x + (2*increment), 210, start_position_x+40 + (2*increment), 250, fill = '#e85a4f'))
						self.node_circles.append(self.w.create_oval(start_position_x + (2*increment), 290, start_position_x+40 + (2*increment), 330, fill = '#e85a4f'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (2*increment), 177, start_position_x+23+ (2*increment), 182, fill = '#e85a4f'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (2*increment), 187, start_position_x+23+ (2*increment), 192, fill = '#e85a4f'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (2*increment), 197, start_position_x+23+ (2*increment), 202, fill = '#e85a4f'))
					if(i == 3):
						self.node_circles.append(self.w.create_oval(start_position_x + (3*increment), 50, start_position_x+40 + (3*increment), 90, fill = '#84ceeb'))
						self.node_circles.append(self.w.create_oval(start_position_x + (3*increment), 130, start_position_x+40 + (3*increment), 170, fill = '#84ceeb'))
						self.node_circles.append(self.w.create_oval(start_position_x + (3*increment), 210, start_position_x+40 + (3*increment), 250, fill = '#84ceeb'))
						self.node_circles.append(self.w.create_oval(start_position_x + (3*increment), 290, start_position_x+40 + (3*increment), 330, fill = '#84ceeb'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (3*increment), 177, start_position_x+23+ (3*increment), 182, fill = '#84ceeb'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (3*increment), 187, start_position_x+23+ (3*increment), 192, fill = '#84ceeb'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (3*increment), 197, start_position_x+23+ (3*increment), 202, fill = '#84ceeb'))
					if(i == 4):
						self.node_circles.append(self.w.create_oval(start_position_x + (4*increment), 50, start_position_x+40 + (4*increment), 90, fill = '#fff652'))
						self.node_circles.append(self.w.create_oval(start_position_x + (4*increment), 130, start_position_x+40 + (4*increment), 170, fill = '#fff652'))
						self.node_circles.append(self.w.create_oval(start_position_x + (4*increment), 210, start_position_x+40 + (4*increment), 250, fill = '#fff652'))
						self.node_circles.append(self.w.create_oval(start_position_x + (4*increment), 290, start_position_x+40 + (4*increment), 330, fill = '#fff652'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (4*increment), 177, start_position_x+23+ (4*increment), 182, fill = '#fff652'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (4*increment), 187, start_position_x+23+ (4*increment), 192, fill = '#fff652'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (4*increment), 197, start_position_x+23+ (4*increment), 202, fill = '#fff652'))
					if(i == 5):
						self.node_circles.append(self.w.create_oval(start_position_x + (5*increment), 50, start_position_x+40 + (5*increment), 90, fill = '#86c232'))
						self.node_circles.append(self.w.create_oval(start_position_x + (5*increment), 130, start_position_x+40 + (5*increment), 170, fill = '#86c232'))
						self.node_circles.append(self.w.create_oval(start_position_x + (5*increment), 210, start_position_x+40 + (5*increment), 250, fill = '#86c232'))
						self.node_circles.append(self.w.create_oval(start_position_x + (5*increment), 290, start_position_x+40 + (5*increment), 330, fill = '#86c232'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (5*increment), 177, start_position_x+23+ (5*increment), 182, fill = '#86c232'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (5*increment), 187, start_position_x+23+ (5*increment), 192, fill = '#86c232'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (5*increment), 197, start_position_x+23+ (5*increment), 202, fill = '#86c232'))
					if(i == 6):
						self.node_circles.append(self.w.create_oval(start_position_x + (6*increment), 50, start_position_x+40 + (6*increment), 90, fill = '#f172a1'))
						self.node_circles.append(self.w.create_oval(start_position_x + (6*increment), 130, start_position_x+40 + (6*increment), 170, fill = '#f172a1'))
						self.node_circles.append(self.w.create_oval(start_position_x + (6*increment), 210, start_position_x+40 + (6*increment), 250, fill = '#f172a1'))
						self.node_circles.append(self.w.create_oval(start_position_x + (6*increment), 290, start_position_x+40 + (6*increment), 330, fill = '#f172a1'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (6*increment), 177, start_position_x+23+ (6*increment), 182, fill = '#f172a1'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (6*increment), 187, start_position_x+23+ (6*increment), 192, fill = '#f172a1'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (6*increment), 197, start_position_x+23+ (6*increment), 202, fill = '#f172a1'))
					if(i == 7):
						self.node_circles.append(self.w.create_oval(start_position_x + (7*increment), 50, start_position_x+40 + (7*increment), 90, fill = '#f79e02'))
						self.node_circles.append(self.w.create_oval(start_position_x + (7*increment), 130, start_position_x+40 + (7*increment), 170, fill = '#f79e02'))
						self.node_circles.append(self.w.create_oval(start_position_x + (7*increment), 210, start_position_x+40 + (7*increment), 250, fill = '#f79e02'))
						self.node_circles.append(self.w.create_oval(start_position_x + (7*increment), 290, start_position_x+40 + (7*increment), 330, fill = '#f79e02'))

						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (7*increment), 177, start_position_x+23+ (7*increment), 182, fill = '#f79e02'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (7*increment), 187, start_position_x+23+ (7*increment), 192, fill = '#f79e02'))
						self.node_circles.append(self.w.create_oval(start_position_x + 18+ (7*increment), 197, start_position_x+23+ (7*increment), 202, fill = '#f79e02'))

				
			except ValueError:
				Invalid_Popup()
		else:
			Invalid_Popup()

	def create_lines(self, i, j):
		num_layers = len(self.layers)
		start_position_x = 350
		increment = 660/(num_layers+2)

		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 50 + 20, start_position_x + (j*increment) + 20, 50+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 50 + 20, start_position_x + (j*increment) + 20, 130+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 50 + 20, start_position_x + (j*increment) + 20, 210+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 50 + 20, start_position_x + (j*increment) + 20, 290+20, fill = '#ffffff'))

		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 130 + 20, start_position_x + (j*increment) + 20, 50+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 130 + 20, start_position_x + (j*increment) + 20, 130+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 130 + 20, start_position_x + (j*increment) + 20, 210+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 130 + 20, start_position_x + (j*increment) + 20, 290+20, fill = '#ffffff'))

		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 210 + 20, start_position_x + (j*increment) + 20, 50+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 210 + 20, start_position_x + (j*increment) + 20, 130+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 210 + 20, start_position_x + (j*increment) + 20, 210+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 210 + 20, start_position_x + (j*increment) + 20, 290+20, fill = '#ffffff'))

		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 290 + 20, start_position_x + (j*increment) + 20, 50+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 290 + 20, start_position_x + (j*increment) + 20, 130+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 290 + 20, start_position_x + (j*increment) + 20, 210+20, fill = '#ffffff'))
		self.node_circles.append(self.w.create_line(start_position_x+ (i*increment)+20, 290 + 20, start_position_x + (j*increment) + 20, 290+20, fill = '#ffffff'))
