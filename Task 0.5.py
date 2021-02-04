import math  
def get_triangle_area(x,y,z):
    s = (x + y + z)*(1/2)   
    area = math.sqrt((s*(s-x)*(s-y)*(s-z))) # Heroins formula for area of a triangle with 3 sides
    return area
area_var = get_triangle_area(3,2,4)
print(area_var)