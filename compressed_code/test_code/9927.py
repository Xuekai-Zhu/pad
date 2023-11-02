def solution():
    
    miles_per_day = 75
    miles_per_gallon = 50
    gallons_per_day = miles_per_day / miles_per_gallon
    price_per_gallon = 3
    days = 10
    total_cost = gallons_per_day * price_per_gallon * days
    result = total_cost
    return result

print(solution())