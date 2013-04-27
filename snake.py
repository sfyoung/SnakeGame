'''
**********************
* shufyoung@gmail.com*
**********************
'''
import sys
import curses
from random import randint

scr = curses.initscr()
snake =[(12, 2), (12, 1), (12, 0)]
arrow = -1

eggy = randint(1, scr.getmaxyx()[0] - 1)
eggx = randint(1, scr.getmaxyx()[1] - 1)

def randegg():
    global eggy, eggx, snake
    while (eggy, eggx) in snake:
        eggx = randint(1, scr.getmaxyx()[1] - 1)
        eggy = randint(1, scr.getmaxyx()[0] - 1)

def showSnake():
	global snake, scr
	for T in snake:
		scr.addstr(T[0], T[1], '*')

def move(direction):
	global snake, arrow
	if direction == ord('j') and (snake[0][1] - 1) != snake[1][1]:
		snake.pop()
		snake.insert(0, (snake[0][0], snake[0][1] - 1))
		arrow = direction
	elif direction == ord('l') and (snake[0][1] + 1) != snake[1][1]:
		snake.pop()
		snake.insert(0, (snake[0][0], snake[0][1] + 1))
		arrow = direction
	elif direction == ord('k') and (snake[0][0] + 1) != snake[1][0]:
		snake.pop()
		snake.insert(0, (snake[0][0] + 1, snake[0][1]))
		arrow = direction
	elif direction == ord('i') and (snake[0][0] - 1) != snake[1][0]:
		snake.pop()
		snake.insert(0, (snake[0][0] - 1, snake[0][1]))
		arrow = direction

def checkState():
	global snake,scr
	T = scr.getmaxyx()
	if snake[0][0] > 0 and snake[0][0] < T[0] and snake[0][1] > 0 and snake[0][1] < T[1] and snake[0] not in snake[1:]:
		return True
	return False

def eatEgg():
	global snake, eggy, eggx
	snake.append((eggy, eggx))
	randegg()

randegg()
showSnake()
scr.addstr(13, 0, 'Press one of j,k,l,i to start')
scr.addstr(eggy, eggx, '&')
scr.refresh()

while 1:
	scr.timeout(200)
	c = scr.getch()
	if c in [ord('j'), ord('k'), ord('l'), ord('i')]:
		move(c)
	elif c == -1:
		move(arrow)
	elif c == ord('q'):
		break

	if snake[0][0] == eggy and snake[0][1] == eggx:
		eatEgg()
		scr.erase()
		scr.addstr(eggy, eggx, '&')
		showSnake()
		continue
	scr.addstr(eggy, eggx, '&')

	if checkState(): 
		scr.erase()
		scr.addstr(eggy, eggx, '&')
		showSnake()
		scr.refresh()
	else:
	    break
curses.endwin()
