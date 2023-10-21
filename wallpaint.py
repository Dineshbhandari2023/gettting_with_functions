height = int(input("Height of the wall: "))
width = int(input("Width of the wall: "))
coverage = 5

import math 

def paint_calc(H, W, C):
    area = height*width
    num_of_can_req = math.ceil(area/coverage)
    print(f"You required {num_of_can_req} paintcans for the wall.")
    
paint_calc(H= height, W=width, C=coverage)    
    
  
    