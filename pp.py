import pygame
from code.quit_window import quit_window
from code.button import Button
from code.initialization import *
from code.label import *

# Button 1 istance
b1 = Button(
	screen, 
	text="Hello",
	position=(100, 100),
	size=40,
	color=(255,255,0),
	command=lambda: print("hello"))

# Label
lb1 = Label(
	screen,
	text="pythonprogramming.altervista.org", 
	position=(50, 360),
	size=20,
	color="white")

def main():
	while True:
		quit_window()
		b1.blit()
		labels_blit()


main()
