import sys
from setting import Setting 
from help import Help
from exit import Exit
from play import Count_Player
from guard.list_guard import List_Guard

class Start:
	def __init__(self) -> None:
		self.optionList = {"play": Count_Player,"setting":Setting,"exit":Exit}
	def __str__(self):
		return("""
		HI,
		Welcome to Mafia Game.
		this game is created by soheil mohseni.




		MENU :
		---> PLAY
		---> SETTING
		---> HELP
		---> EXIT

		""")
	def	choose_Menu(self):
		check = False
		while check == False:
			self.item = input("Choose an option:\t")		
			checker = List_Guard(self.optionList,self.item)
			check = checker.guard()
		count_player= self.optionList[self.item]()


def boot_Game():
	start_Game = Start()
	print (start_Game)
	start_Game.choose_Menu()

boot_Game()
