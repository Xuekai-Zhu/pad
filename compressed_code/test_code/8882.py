def solution():
    
    total_miles = 10 + 6 + 5 + 9
    miles_per_gallon = 15
    gallons_needed = total_miles / miles_per_gallon
    cost_per_gallon = 3.5
    total_cost = gallons_needed * cost_per_gallon
    result = total_cost
    return result

print(solution())