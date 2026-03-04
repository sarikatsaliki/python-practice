#parent class 
class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,"is" ,self.age, "years old")
#child class    
class cat(pet):
     def __init__(self,name,age, breed):
         super().__init__(name,age) #constructor of parent class
         self.breed = breed
     def details(self):
         print(self.name, "is", self.age, "years old" ,"and it is a", self.breed)
p1 = cat("milly",5,"raggdoll") #object 1
p2 = cat("billy", 6,"Birman") #object 2
p1.show()
p2.details()


