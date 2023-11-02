def solution():
     bill_red_mushrooms = 12
     bill_brown_mushrooms = 6
     ted_green_mushrooms = 14
     ted_blue_mushrooms = 6
    
     red_mushrooms_spotted = bill_red_mushrooms * (2/3)
     brown_mushrooms_spotted = bill_brown_mushrooms
     blue_mushrooms_spotted = ted_blue_mushrooms * (1/2)
    
     total_mushrooms_spotted = red_mushrooms_spotted + brown_mushrooms_spotted + blue_mushrooms_spotted
     result = total_mushrooms_spotted
     return result

print(solution())