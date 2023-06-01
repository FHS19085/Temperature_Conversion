from tkinter import *


class Converter:

	def __init__(self):

		button_font = ("Arial", "12", "bold")
		button_fg = "#FFFFFF"

		# Set up GUI frame
		self.temp_frame = Frame()
		self.temp_frame.grid()

		self.temp_heading = Label(self.temp_frame,
		                          text="Temperature Converter",
		                          font=("Arial", "16", "bold"))
		self.temp_heading.grid(row=0)

		instructions = "Please enter a temperature below and " \
           "then press one of the buttons to convert " \
           "it from Centergrade to Fahreinheit."
		self.temp_instructions = Label(self.temp_frame,
		                               text=instructions,
		                               wrap=250,
		                               width=40,
		                               justify="left")

		self.temp_instructions.grid(row=1)
		self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))

		self.temp_entry.grid(row=2, padx=10, pady=10)

		error = "Please enter a valid number"
		self.temp_error = Label(self.temp_frame, text="", fg="#9C0000")
		self.temp_error.grid(row=3)

		self.button_frame = Frame(self.temp_frame)
		self.button_frame.grid(row=4)

		self.to_celcius_button = Button(self.button_frame,
		                                text="To Degrees C",
		                                bg="#FF66FF",
		                                fg=button_fg,
		                                font=button_font,
		                                width=12,
		                                command=self.to_celsius)
		self.to_celcius_button.grid(row=0, column=0, padx=5, pady=5)

		self.to_farenheit_button = Button(self.button_frame,
		                                  text="To Farenheit",
		                                  bg="#FF66B3",
		                                  fg=button_fg,
		                                  font=button_font,
		                                  width=12)
		self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

		self.to_help_button = Button(self.button_frame,
		                             text="Help / Info",
		                             bg="#FF66B3",
		                             fg=button_fg,
		                             font=button_font,
		                             width=12)
		self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

		self.to_history_button = Button(self.button_frame,
		                                text="History / Export",
		                                bg="#FF66FF",
		                                fg=button_fg,
		                                font=button_font,
		                                width=12,
		                                state=DISABLED)
		self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

	def check_temp(self, min_value):
		error = "Please enter a number that is more " \
  "than {}".format(min_value)

		try:
			response = self.temp_entry.get()
			response = float(response)
			
			if response < min_value:
				self.temp_error.config(text=error)

			else:
				return response

		except ValueError:
			self.temp_error.config(text=error)
		
	def to_celsius(self):
		self.check_temp(-459)
		
# Main Routine
if __name__ == "__main__":
	root = Tk()
	root.title("Temperature Converter")
	Converter()
	root.mainloop()
