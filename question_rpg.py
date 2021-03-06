import random
import os
import sys
import cmd


class Knight:
	def __init__(self,name,lv,max_hp,attack,defense,exp):
		self.name=name
		self.lv=lv
		self.max_hp=max_hp
		self.hp=max_hp
		self.attack=attack
		self.defense=defense
		self.exp=exp
		self.max_exp=30
		self.kills=0
		self.potion=0
		self.sword=0
		self.armor=0

	def stats(self):
		print('--------------------------------')
		print("Welcome " + self.name,"this are your stats:")
		print(" Lv=", self.lv,'next',self.exp,'/',self.max_exp, "\n hp=",self.hp, "\n attack=",self.attack, "\n defense=",self.defense)
		print('--------------------------------')

	def inventory(self):
		while self.hp >0:
			selct_item=input(f'What you want to use? \na.potion {self.potion} \nb.armor {self.armor} \nc.sword {self.sword} \nd.Exit \nChoice: ')
			print('--------------------------------')

			# use potion
			if selct_item.lower() == 'a' or selct_item.lower() == 'potion':
				if self.potion>0:
					self.hp += 20
					self.potion-=1
					print('Hp: ',self.hp)
					print('--------------------------------')
				else:
					print('You have no potion to use')
					print('--------------------------------')

			# equip armor
			elif selct_item.lower() == 'b' or selct_item.lower() == 'armor':
				if self.armor>0:
					self.defense += random.randint(1,15)
					self.armor-=1
					print('Def: ',self.defense)
					print('--------------------------------')
				else:
					print("You don't have an armor to equip")
					print('--------------------------------')

			# equip sword
			elif selct_item.lower() == 'c' or selct_item.lower() == 'sword':
				if self.sword>0:
					self.attack += random.randint(1,15)
					self.sword-=1
					print('Atk: ',self.attack)
					print('--------------------------------')
				else:
					print("You don't have a sword to equip")
					print('--------------------------------')

			# exit
			elif selct_item.lower() =='d' or selct_item.lower() =='Exit':
				break

		print('This are your stats \nHp: ', self.hp,'\nattack power: ',self.attack, '\ndef: ',self.defense)
		print('--------------------------------')

	def levelUp(self):
		self.kills+=1
		# randon reward drop
		if self.kills +1:
			rewards=['potion','sword','armor','']
			rew_drop=rewards[random.randint(0,3)]

			if rew_drop == rewards[0]:
				self.potion+=random.randint(1,4)
				print('--------------------------------')
				print("You won a: ",rew_drop)
				print('--------------------------------')
			elif rew_drop == rewards[1]:
				self.sword+=1
				print('--------------------------------')
				print("You won a: ",rew_drop)
				print('--------------------------------')
			elif rew_drop == rewards[2]:
				self.armor+=1
				print('--------------------------------')
				print("You won an: ",rew_drop)
				print('--------------------------------')
			else:
				print('Your enemy dont drop anything')
				print('--------------------------------')

		# level up
		self.exp+= random.randrange(10,30,5)
		print("This is  your exp:",self.exp)

		if self.exp >= self.max_exp:
			self.max_hp+=self.max_hp/2
			self.hp+=10
			self.lv += 1
			self.attack+=5
			self.kills+=1
			print("Current attack power: ",self.attack)
			print("You have leveled up")
			print('--------------------------------')
			print("Now you are level: ",self.lv)
			self.max_exp += self.hp *2
			print("For reach the next level you need to collect", int(self.max_exp),'of exp')
			print('--------------------------------')
		
class Enemy:
	def __init__(self,name,lv,hp,attack,defense):
		self.name=name
		self.lv=lv
		self.hp=hp
		self.attack=attack
		self.defense=defense 

	def stats(self):
		print(self.name)
		print(" Lv=", self.lv, "\n hp=",self.hp, '\n atk=',self.attack)

	def lv_up(self):
		self.hp += 10
		self.lv += 1
		self.attack += 3
		self.defense += 3

	def spawn(self):
		self.hp += random.randint(5,15)
		self.attack += random.randint(5,10)
		self.defense += random.randint(1,8)

	def dead(self):
		if self.hp <=0:	
			print('Congratulations you have killed your enemy')
			print('--------------------------------')

def battle_choice(question,player,enemy):
	print('--------------------------------')
	player_turn=input(question +'\n a.Attack \n b.Defend \n c.Run \n d.Inventory \n e.Player \nAction:')
	print('--------------------------------')

	# attack choice
	if player_turn.lower() == 'a' or player_turn.lower() == 'attack':
		damage= player.attack - enemy.defense
		enemy.hp-= damage
		print("You attacked the enemy")

		if enemy.hp >0:
			print("Enemy remaining hp:",enemy.hp)
			print('--------------------------------')

			print("The enemy attacked you")
			if player.defense > enemy.attack:
				player_dmg=player.defense - enemy.attack
				player.hp=player.hp - player_dmg
				if player.hp >0:
					print("Player remaining health:",player.hp)
					print('--------------------------------')
				else:
					print('0 hp')
					print('--------------------------------')

			elif player.defense < enemy.attack:
				player_dmg=enemy.attack - player.defense
				player.hp=player.hp-player_dmg
				if player.hp >0:
					print("Player remaining health:",player.hp)
					print('--------------------------------')
				else:
					print('0 hp')
					print('--------------------------------')

	# defense choice
	elif player_turn.lower() == 'b' or player_turn.lower()=='defend':
		player.defense + 5	

		if player.defense > enemy.attack:
			player_dmg=player.defense - enemy.attack
			player.hp=player.hp - player_dmg
			if player.hp >0:
				print("You are in defense mode")
				print("Player remaining health:",player.hp)
				print('--------------------------------')
			else:
				print('0 hp')
				print('--------------------------------')

		elif player.defense < enemy.attack:
			player_dmg=enemy.attack - player.defense
			player.hp=player.hp-player_dmg
			if player.hp >0:
				print("You are in defense mode")
				print("Player remaining health:",player.hp)
				print('--------------------------------')
			else:
				print('0 hp')
				print('--------------------------------')
			
	# run
	elif player_turn.lower() == 'c' or player_turn.lower()== 'run':
		print("You run away")
		print('--------------------------------')
		player.stats()

	# inventory choice
	elif player_turn.lower() =='d' or player_turn.lower()=='inventory':
		print('--------------------------------')
		print('What item doy you want to do?')
		player.inventory()
		print('--------------------------------')

	elif player_turn.lower()== 'e' or player_turn.lower()=='player':
		print('--------------------------------')
		player.stats()

	else:
		pass