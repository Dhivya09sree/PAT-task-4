  
class Circle:#circule class create
      
    def __init__(self, radius_list):
        # Constructor method to initialize the radius_list attribute
        self.radius_list = radius_list

    
    def calculate_area(self):
        pi=3.141 # assing PI value 
        # Method to calculate and print the area of circles for each radius in the radius_list
        for radius in self.radius_list: #take the value from raddi list one by one 
            area = pi * (radius ** 2)  # Calculate the area using the formula πr^2
            print("Area of circle with radius", radius, ":", area)  # Print the calculated area

# list of radii
radii = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an instance of the Circle class with the provided list of radii
circle = Circle(radii)

# Call the calculate_area method on the circle object to calculate and print the areas
circle.calculate_area() 





