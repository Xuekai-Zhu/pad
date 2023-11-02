def solution():
    
    city_miles = 60
    highway_miles = 200
    city_mpg = 30
    highway_mpg = 40
    gas_price = 3.00
    city_gallons = city_miles / city_mpg
    highway_gallons = highway_miles / highway_mpg
    total_gallons = (2 * city_gallons) + (2 * highway_gallons)
    total_cost = total_gallons * gas_price
    result = total_cost
    return result

print(solution())