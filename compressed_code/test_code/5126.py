def solution():
    
    previous_weight = 6.4
    giant_weight = 2.5 * previous_weight
    leg_area = 0.5
    pressure = giant_weight / (8 * leg_area)  
    result = pressure
    return result

print(solution())