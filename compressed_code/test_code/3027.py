def solution():
    
    mpg = 25
    miles_per_week = 50 * 5
    gallons_per_week = miles_per_week / mpg
    tank_size = 10
    total_weeks = 4
    total_gallons = gallons_per_week * total_weeks
    cost_per_gallon = 2
    total_cost = total_gallons * cost_per_gallon
    result = total_cost
    return result

print(solution())