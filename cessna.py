from vehicle import Vehicle

# Propellor light aircraft
class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def drive(self):
        print("Dang ole plane making propeller noises.")