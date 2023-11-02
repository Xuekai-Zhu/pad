def solution():
    
    total_cost = 135
    table_cost = 55
    num_chairs = 4
    chair_cost = (total_cost - table_cost) / num_chairs
    result = chair_cost
    return result

print(solution())