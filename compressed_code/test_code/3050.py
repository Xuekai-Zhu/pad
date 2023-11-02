def solution():
    
    total_distance = 10 + 6 + 5 + 9
    gallon_per_mile = 1 / 15
    total_gallon_needed = total_distance * gallon_per_mile
    cost_per_gallon = 3.50
    total_cost = total_gallon_needed * cost_per_gallon
    result = total_cost
    return result

print(solution())