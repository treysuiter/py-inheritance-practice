from vehicle import Vehicle

# Electric motorcycle
class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def drive(self):
        print("Socially conscious motorcycle goes wrrrrrrrrrrrreeeeeeeeeeee.")