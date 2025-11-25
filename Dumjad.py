from abc import ABC, abstractmethod

class Tomato():
    def type(self):
        print("Vegetable")
    def color(self):
        print("Red")

class Apple():
    def type(self):
        print("Fruit")
    def color(self):
        print("Red")

def func(obj):
    obj.type()
    obj.color()

obj_tomato = Tomato()
obj_apple = Apple()


for obj in (obj_tomato, obj_apple):
    print("=" * 50)
    
    print(f"Is instance of ABC: {isinstance(obj, ABC)}")
   
    print(f"Class name: {type(obj).__name__}")
    
    print(f"\nAttributes:")
    for attr in dir(obj):
        if not attr.startswith('_') and not callable(getattr(obj, attr)):
            print(f"  - {attr}: {getattr(obj, attr)}")
    
    print(f"\nMethods:")
    for method in dir(obj):
        if not method.startswith('_') and callable(getattr(obj, method)):
            print(f"  - {method}()")
    
    print("\nCalling methods:")
    func(obj)
    print()