import math
from guard.list_guard import List_Guard
from guard.mafia_guard import Mafia_Gaurd
class Mafia_Chrachter: 
    def __init__(self,count) -> None:
        self.mafia_List = []
        self.count = math.floor(count / 3)
        self.mafia_Chrachter = ["God_Father","Negotiator","Simple_Mafia","silencor" ,"Thief","HostageـTaker"]
        print("lists of Mafia chraters")
        print(self.mafia_Chrachter)

    def add_Mafia(self,name):
        check = False
        # check_Count_Mafia = Mafia_Gaurd


        # check the validation of the choices
        while (check == False):
            choice = input("add mafia name chrachter or wirte delete for deleting chrachter ?\t")
            if choice == "delete":
                if len(self.mafia_List) > 0:
                    check_Delete = False
                    while (check_Delete == False):
                        delete_Choice = input("write which chrachter do you want to delete // write c for cancel that.")
                        if delete_Choice == "c":
                            delete_Choice = None
                            break
                        checker_Choice = List_Guard(self.mafia_Chrachter,delete_Choice)
                        check_Delete = checker_Choice.guard()
                    if delete_Choice:
                        self.mafia_Chrachter.remove()
                        continue
                    else:
                        continue
                else:
                    print("you didn't add anyone for mafia List")
                    continue
            check_validation =  List_Guard(self.mafia_Chrachter,choice)
            

            check = checker.guard(choice,self.mafia_List)

         # check the for the duplication choices
        # check = False
        # while (check == False):
        #     choice = input("how many players are in game?\t")
        #     checker = List_Guard(self.mafia_Chrachter,choice)
        #     check = checker.guard(choice,self.mafia_List)
        
        # if(name in self.mafia_Chrachter):
        #     if(name in self.mafia_List):
        #         if(check_Count_Mafia.guard()):
        #             self.mafia_List.append(name)
        #         else:
        #             print("you can't add more mafia")
        #     else:
        #         print("DUPLICATE ERROR.you have added this Chrachter before.")
        # else:
        #     print("it's not valid value.")
      