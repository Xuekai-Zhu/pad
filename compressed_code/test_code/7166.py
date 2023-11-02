def solution():
    
    shrimp_per_guest = 5
    total_guests = 40
    shrimp_per_pound = 20
    cost_per_pound = 17.00
    total_shrimp = shrimp_per_guest * total_guests
    total_pounds = total_shrimp / shrimp_per_pound
    total_cost = total_pounds * cost_per_pound
    result = total_cost
    return result

print(solution())