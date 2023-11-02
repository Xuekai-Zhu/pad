def solution():
    miles_per_gallon = 50
    miles_driven_per_day = 75
    price_per_gallon = 3
    days = 10
    total_miles_driven = miles_driven_per_day * days
    total_gallons_used = total_miles_driven / miles_per_gallon
    total_cost = total_gallons_used * price_per_gallon
    result = total_cost
    return result

print(solution())