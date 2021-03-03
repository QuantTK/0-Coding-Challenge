import math  
def get_triangle_area(x,y,z):
    semi_perimeter = (x + y + z)*(1/2)   
    area = math.sqrt((semi_perimeter*(semi_perimeter-x)*(semi_perimeter-y)*(semi_perimeter-z))) # Heroins formula for area of a triangle with 3 sides
    return area
