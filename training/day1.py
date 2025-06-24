class car:
    def __init__(self, Brand, model, years):
        self.Brand = Brand
        self.model = model
        self.years = years
        self.speed = 0

    def Accelerate(self):
        self.speed = 180
        print("speed is equal 180")
        return self.speed

    def Brake(self):
        self.speed -= 10
        return self.speed

    def display(self):
        return f"Brand: {self.Brand}, Model: {self.model}, Years: {self.years}, Speed: {self.speed}"
    
car1 = car('BMWx6', 'german', 2022)
car2 = car('marsedes', 'german', 2020)

print(car1.Accelerate())
