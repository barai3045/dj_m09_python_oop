class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        
    def update_odometer(self, om):
        if om > self.odometer:
            self.odometer = om
        else:
            print("Can't update odometer")
        
    def __str__(self):
        return "The Car is {} {} and Year: {}".format(self.make, self.model, self.year)
    
    def __eq__(self, value):
        return self.make == value.make and self.model == value.model and self.year == value.year
    
c1 = Car('Toyota', 'Camry', 2023)
c2 = Car('Toyota', 'Camry', 2023)



"""inherient class"""
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")
        
        
class Reptile(Animal): 
    def __init__(self, name):
        self.name = name 
        
    def eat(self):
        print(f"I don't eat, I bite!")
        
    def crawl(self):
        print(f"{self.name} is crawling") 
        
class Crocodile(Reptile):
    pass

class Snake(Reptile):
    pass
        
a1 = Reptile("Russel Viper")

a1.eat()
a1.crawl()