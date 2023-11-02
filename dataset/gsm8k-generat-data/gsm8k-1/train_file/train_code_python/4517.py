def solution():
    """Carl is figuring out how much he'll need to spend on gas for his upcoming road trip to the Grand Canyon. His car gets 30 miles per gallon in cities and 40 miles per gallon on the highway. The distance from his house to the Grand Canyon, one way, is 60 city miles and 200 highway miles. If gas costs $3.00 per gallon, how much will Carl need to spend?"""
    
    city_miles = 60
    highway_miles = 200
    city_gas_mileage = 30
    highway_gas_mileage = 40
    gas_cost_per_gallon = 3.00
    
    total_city_gallons = city_miles / city_gas_mileage
    total_highway_gallons = highway_miles / highway_gas_mileage
    total_gallons = total_city_gallons + total_highway_gallons
    total_cost = total_gallons * gas_cost_per_gallon
    
    result = total_cost
    return result

print(solution())