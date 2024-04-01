from tkinter import *
import numpy as np
from PIL import ImageGrab

# Clears the canvas
def clear_widget():
	global cv, l1
	cv.delete("all")
	l1.destroy()


# Activate canvas
def event_activation(event):
	global lastx, lasty
	cv.bind('<B1-Motion>', draw_lines)
	lastx, lasty = event.x, event.y


# To draw on canvas
def draw_lines(event):
	global lastx, lasty
	x, y = event.x, event.y
	cv.create_line((lastx, lasty, x, y), width=5, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=12)
	lastx, lasty = x, y

window = Tk()
window.title("Canvas")
L1 = Label(window, text="Write by dragging", font=('Algerian', 25), fg="blue")
L1.place(x=35, y=10)

# Button to clear canvas
b1 = Button(window, text="Clear Canvas", font=('Algerian', 15), bg="orange", fg="black", command=clear_widget)
b1.place(x=120, y=570)

# Setting properties of canvas
cv = Canvas(window, width=800, height=500, bg='green')
cv.place(x=120, y=70)

cv.bind('<Button-1>', event_activation)
window.geometry("600x500")
window.mainloop()

lastx, lasty = None, None


