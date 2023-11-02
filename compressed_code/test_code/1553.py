def solution():
    
    distance_1 = 2 * 60
    distance_2 = 3 * 50
    total_distance = distance_1 + distance_2
    gallons_used = total_distance / 30
    cost_per_gallon = 2
    total_cost = gallons_used * cost_per_gallon
    result = total_cost
    return result

print(solution())