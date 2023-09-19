from guard.list_guard import Int_Gaurd

class Count_Player:
	def __init__(self):
		self.check = False
		self.list_Name = []
		while self.check == False:
			count = input("how many players are in game?\t")
			checker = Int_Gaurd(count)
			self.check = checker.gaurd()
		self.enter_player()

	def enter_player(self):
		for player in range(self.check):
			name =  input("enter player "+ str(player +1) +" name: \t")
			self.list_Name.append(name)
		print("participators:" )
		print(self.list_Name)
		
		# except Exception as e:


# Count_Player.count = 0

