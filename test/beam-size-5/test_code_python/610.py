def solution():
    
    weeks_per_year = 52
    gallons_per_load = 20
    cost_per_gallon = 0.15
    total_gallons = weeks_per_year * gallons_per_load
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())