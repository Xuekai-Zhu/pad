def solution():
    shrimp_per_guest = 5
    guests = 40
    shrimp_per_pound = 20
    cost_per_pound = 17
    pounds_needed = (shrimp_per_guest * guests) / shrimp_per_pound
    total_cost = pounds_needed * cost_per_pound
    result = total_cost
    return result

print(solution())