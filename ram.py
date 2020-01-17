from vehicle import Vehicle

# Gas powered truck
class Ram(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0
    
    def drive(self):
        print("Big ole truck coming thru hollerin out rwaaararraraararrumduddum.")