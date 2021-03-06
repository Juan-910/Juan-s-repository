from question_rpg import Knight,Enemy,battle_choice
import random
import sys
import os
import cmd

screen_width=100

def title_options():
	option=input('> ')
	if option.lower() == 'play':
		os.system('cls')
		start_game()
	elif option.lower()	== 'exit':
		sys.exit()
	while option.lower() not in ['play','exit']:
		print('Please select one of the options above')
		option=input('> ')
		if option.lower() == 'play':
			start_game()
		elif option.lower()	== 'exit':
			sys.exit()

def title_screen():
	os.system('cls')
	print('--------------------------------')
	print('    *Welcome to the text RPG*   ')
	print('--------------------------------')
	print('	    - play -			   ')
	print('	    - exit -			   ')
	print('-----Game made by TCR-Shu12-----')
	title_options()

def start_game():
	adventurer=Knight('adventurer',1,50,20,8,0)
	adventurer.stats()
	
	foes=['goblin','wizard','lizard','troll']
	foe=Enemy(foes[random.randrange(0,3,1)],1,10,5,5)
	foe.stats()

	while adventurer.hp >0:
		print('--------------------------------')
		battle_choice('\nWhat you are going to do?\n',adventurer,foe)
		print('--------------------------------')

		if foe.hp <=0:
			foe.dead()
			adventurer.levelUp()
			print('A new enemy has arrive')
			foe.spawn()
			foe.lv_up()
			foe.stats()

		elif adventurer.hp<=0:
			print('********************')
			print("You have been killed")
			print('********************')
			print('GAME OVER!!!')
			title_screen()
			break

def game():
	title_screen()

game()