#parent class 
class Smartphone:
    def __init__(self, battery_level):
        self.__battery_level = battery_level
    def charge(self): #Increases battery level by 10
        self.__battery_level += 10
        print("battery increased to:", self.__battery_level )
    def call(self): #decrease battery level ny 5
        self.__battery_level -= 5
        print("battery decreased to:", self.__battery_level)
    def get_battery(self): #method to check battery 
        return  self.__battery_level
s1 = Smartphone(50)
s1.call()
print(s1.get_battery())