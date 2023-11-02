def solution():
    mpg_city = 30
    mpg_highway = 40
    miles_city = 60
    miles_highway = 200
    price_per_gallon = 3
    gallons_city = miles_city / mpg_city
    gallons_highway = miles_highway / mpg_highway
    cost_city = gallons_city * price_per_gallon
    cost_highway = gallons_highway * price_per_gallon
    total_cost = cost_city + cost_highway
    result = total_cost
    
    return result

print(solution())