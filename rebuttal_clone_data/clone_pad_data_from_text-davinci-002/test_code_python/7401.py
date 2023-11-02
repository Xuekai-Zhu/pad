def solution():
    tank1_capacity = 7000
    tank2_capacity = 5000
    tank3_capacity = 3000
    
    tank1_contents = tank1_capacity * 3/4
    tank2_contents = tank2_capacity * 4/5
    tank3_contents = tank3_capacity * 1/2
    
    total_gallons = tank1_contents + tank2_contents + tank3_contents
    
    result = total_gallons
    
    return result

print(solution())