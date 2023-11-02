def solution():
    
    total_cost = 130 - 4
    chair_quantity = 3
    table_cost = 50
    plate_cost = 20*2
    chair_cost = (total_cost - table_cost - plate_cost) / chair_quantity
    result = chair_cost
    return result

print(solution())