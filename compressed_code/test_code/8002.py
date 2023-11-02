def solution():
    
    cars_repaired = 5
    standard_repair_time = 40 
    increased_repair_time = (1.5 * standard_repair_time) 
    standard_repair_count = 3
    increased_repair_count = cars_repaired - standard_repair_count
    standard_repair_cost = (standard_repair_count * standard_repair_time) / 60 * 20
    increased_repair_cost = (increased_repair_count * increased_repair_time) / 60 * 20
    total_repair_cost = standard_repair_cost + increased_repair_cost
    result = total_repair_cost
    return result

print(solution())