def solution():
    
    glasses_per_gallon = 16
    cost_per_gallon = 3.50
    gallons_made = 2
    glasses_made = gallons_made * glasses_per_gallon
    glasses_sold = glasses_made - 5 - 6
    revenue = glasses_sold * 1
    cost = gallons_made * cost_per_gallon
    profit = revenue - cost
    result = profit
    return result

print(solution())