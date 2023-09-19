from list_guard import ma
class List_Guard:
    def __init__(self, data_list, data):
        self.data_list = data_list
        self.data = data
        # print("??????????", self.data_list)
    def guard(self,data,data_list):
        if data in data_list:
            return True
        else:
            print("it's not a valid option")
            return False
class Int_Gaurd:
    def __init__(self,data):
        self.data = data
    def gaurd(self):
        try:
            return int(self.data)
        except:
            print(" it's not valid value")
            return False
        
class Duplicate_Guard:
    def duplicate_Guard(self,data, data_List):
        if data not in data_List:
            return True
        else :
            return False
