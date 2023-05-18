from tkinter import *


class Converter:

	def __init__(self):

		# Set up GUI frame
		self.temp_frame = Frame()
		self.temp_frame.grid()

		self.temp_heading = Label(self.temp_frame,
		                          text="Temperature Converter",
		                          font=("Arial", "bold", "16"))
		self.temp_heading.grid(row=0)

		instructions = "Please enter a temperature below and " \
           "then press one of the buttons to convert " \
           "it from Centergrade to Fahreinheit."
		self.temp_instructions = Label(self.temp_frame,
		                               text=instructions,
		                               wrap=250,
		                               width=40,
		                               justify="Left")

		self.temp_instructions.grid(row=1)


# Main Routine
if __name__ == "__main__":
	root = Tk()
	root.title("Temperature Converter")
	Converter()
	root.mainloop()
