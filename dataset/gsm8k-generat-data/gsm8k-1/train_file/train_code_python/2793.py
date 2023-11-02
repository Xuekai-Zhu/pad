def solution():
    """John repairs 5 cars. 3 of the cars take 40 minutes each to repair. The remaining ones take 50% longer each to repair. He makes $20 per hour repairing cars. How much money does he make?"""
    cars_repaired = 5
    standard_repair_time = 40 # in minutes
    increased_repair_time = (1.5 * standard_repair_time) # in minutes
    standard_repair_count = 3
    increased_repair_count = cars_repaired - standard_repair_count
    standard_repair_cost = (standard_repair_count * standard_repair_time) / 60 * 20
    increased_repair_cost = (increased_repair_count * increased_repair_time) / 60 * 20
    total_repair_cost = standard_repair_cost + increased_repair_cost
    result = total_repair_cost
    return result

print(solution())