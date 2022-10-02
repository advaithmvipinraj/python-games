from random import randint
import pygame
import pgzero
import pgzrun
import time

apple = Actor("apple")
fail_count = 0
win_count = 0
game_over = False


def draw():
	global win_count
	global fail_count
	global game_over
	
	screen.fill("green")
	apple.draw()
	screen.draw.text("Good Shot: " + str(win_count), color="black", topleft=(10, 10))
	screen.draw.text("You Missed: " + str(fail_count), color="black", topleft=(10, 50))

	if game_over:
		if win_count == 7:
			screen.fill("blue") 
			screen.draw.text("You Won: " + str(win_count), topleft=(10, 10), fontsize=30)

		if fail_count == 3:
			screen.fill("blue") 
			screen.draw.text("You Lost: " + str(fail_count), topleft=(10, 10), fontsize=30)


def place_apple():
	apple.x = randint(10, 800)
	apple.y = randint(10, 600)

def on_mouse_down(pos):
	global win_count
	global fail_count
	global game_over
	

	if apple.collidepoint(pos):
		
		win_count = win_count + 1	

		if win_count == 3:
			game_over = True

		place_apple()

	else:
		fail_count = fail_count + 1
		
		if fail_count == 3:
			game_over = True

		place_apple()

place_apple()
pgzrun.go()
