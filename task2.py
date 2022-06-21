# parasyti klase kuri apibudintu matavimo vienetus(astumas, svoris)

class Dimensions:
    def __init__(self, distance: int, weight: int):
        self.distance = distance
        self.weight = weight 
        
    def print_dimensions(self):
        print(f'Distance is: {self.distance}, Weight is: {self.weight}')
        
    def converter(self):
       new_weight = self.weight * 1000
       print(f'Weight converted in grams: {new_weight}')
        

dimensions = Dimensions(distance = 55, weight =65)

dimensions.print_dimensions()
dimensions.converter()