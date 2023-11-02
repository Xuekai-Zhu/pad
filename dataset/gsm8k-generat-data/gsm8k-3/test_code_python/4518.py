def solution():
    """Carl is figuring out how much he'll need to spend on gas for his upcoming road trip to the Grand Canyon. His car gets 30 miles per gallon in cities and 40 miles per gallon on the highway. The distance from his house to the Grand Canyon, one way, is 60 city miles and 200 highway miles.  If gas costs $3.00 per gallon, how much will Carl need to spend?"""
    # Define the car's mileage in city and highway
    CITY_MILEAGE = 30
    HIGHWAY_MILEAGE = 40

    # Define the distance of the trip
    city_distance = 60
    highway_distance = 200
    total_distance = city_distance + highway_distance

    # Calculate the amount of gas needed for each part of the trip
    city_gas = city_distance / CITY_MILEAGE
    highway_gas = highway_distance / HIGHWAY_MILEAGE

    # Calculate the total amount of gas needed for the entire trip
    total_gas = city_gas + highway_gas

    # Calculate the total cost of gas for the entire trip
    gas_cost = total_gas * 3

    # Display the total cost of gas for the entire trip
    result = gas_cost
    return result

print(solution())