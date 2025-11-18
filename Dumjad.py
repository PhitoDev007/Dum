from abc import ABC, abstractmethod

class bee(ABC):
    @abstractmethod
    def fly(self):  
        pass
    
    def attack(self):
        print("Attack against the intruder")

class honey_bee(bee):
    def fly(self):
        print("looking for feed")

class hornet(bee):
    def fly(self):
        print("looking for enemy")

print("Test 2:")
hb = honey_bee()
hb.fly()
hb.attack()

print("Test 3:")
hb2 = hornet() 
hb2.fly()
hb2.attack()