class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed", School_bus.max_speed,"Mileage:", School_bus.mileage)
class Bird:
    def __init__(self):
        print("Bird is ready")
        def whoisthis(self):
            print("Bird")
        def swim(self):
            print("swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("Penguin")
        def run(self):
            print("Run faster")
peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()
