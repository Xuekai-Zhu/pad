def solution():
    """Carl is figuring out how much he'll need to spend on gas for his upcoming road trip to the Grand Canyon.
    His car gets 30 miles per gallon in cities and 40 miles per gallon on the highway.
    The distance from his house to the Grand Canyon, one way, is 60 city miles and 200 highway miles.
    If gas costs $3.00 per gallon, how much will Carl need to spend?"""
    
    # Define the car's mileage and the distance of the trip
    city_mileage = 30
    highway_mileage = 40
    city_distance = 60
    highway_distance = 200
    
    # Calculate the amount of gas required for the trip
    city_gas = city_distance / city_mileage
    highway_gas = highway_distance / highway_mileage
    total_gas = city_gas + highway_gas
    
    # Calculate the total cost of the gas
    gas_price = 3.00
    total_cost = total_gas * gas_price
    
    result = round(total_cost, 2)
    return result

print(solution())