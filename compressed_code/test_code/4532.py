def solution():
    
    repair_cost = 10
    corner_light_cost = 2 * repair_cost
    brake_disk_cost = 3 * corner_light_cost
    total_parts_cost = corner_light_cost + (2 * brake_disk_cost)
    total_savings = total_parts_cost + repair_cost + 480
    result = total_savings
    return result

print(solution())