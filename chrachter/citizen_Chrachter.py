import math

class Citizen_Chrachter: 
    def __init__(self,count) -> None:
        self.citizen_List = []
        # self.guard(count)
        self.citizen_Chrachter = ["doctor","detective","sniper","armored" ,"baker","reporter","gunman","bomber"]
        self.count = count - math.floor(count / 3) 
    def guard(self): 
        if self.count >= len(self.citizen_List):
            return True
        else:
            return False
    def add_Mafia(self,name):
        if(name in self.citizen_Chrachter):
            if(self.guard()):
                self.citizen_List.append(name)
            else:
                print("you can't add more mafia")
        else:
            print("DUPLICATE ERROR.you have added this Chrachter before.")
    

