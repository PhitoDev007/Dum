class PET:
    def __init__(self, age, weight, gender):
        self.age = age
        self.weight = weight
        self.gender = gender
    def show_all_information(self):
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Gender: {self.gender}")
class Dog(PET):
    def __init__(self, age, weight, gender, fang_size):
        super().__init__(age, weight, gender)
        self.fang_size = fang_size
    def show_all_information(self):
        super().show_all_information()
        print(f"Fang size: {self.fang_size}")
class Cat(PET):
    def __init__(self, age, weight, gender, fang_size):
        super().__init__(age, weight, gender)
        self.fang_size = fang_size
    def show_all_information(self):
        super().show_all_information()
        print(f"Fang size: {self.fang_size}")
class Bird(PET):
    def __init__(self, age, weight, gender, wing_size):
        super().__init__(age, weight, gender)
        self.wing_size = wing_size
    def show_all_information(self):
        super().show_all_information()
        print(f"Wing size: {self.wing_size}")