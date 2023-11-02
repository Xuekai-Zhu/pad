def solution():
    
    shrimp_per_guest = 5
    total_guests = 40
    shrimp_per_pound = 20
    cost_per_pound = 17
    total_shrimp = shrimp_per_guest * total_guests
    pounds_of_shrimp = total_shrimp / shrimp_per_pound
    total_cost = pounds_of_shrimp * cost_per_pound
    result = total_cost
    return result

print(solution())