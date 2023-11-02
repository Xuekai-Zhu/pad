def solution():
    """Carl is figuring out how much he'll need to spend on gas for his upcoming road trip to the Grand Canyon. His car gets 30 miles per gallon in cities and 40 miles per gallon on the highway. The distance from his house to the Grand Canyon, one way, is 60 city miles and 200 highway miles. If gas costs $3.00 per gallon, how much will Carl need to spend?"""
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