def solution():
    
    miles_per_day = 75
    miles_per_gallon = 50
    gallons_per_day = miles_per_day / miles_per_gallon
    gas_price = 3
    total_cost = gallons_per_day * gas_price * 10
    result = total_cost
    return result

print(solution())