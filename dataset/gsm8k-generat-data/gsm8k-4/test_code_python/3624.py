def solution():
    """A truck driver’s heavy semi truck can go 3 miles per gallon of gas.
    The truck driver needs to put gas in his truck at one gas station,
    but wants to put the minimum amount he needs to get him to a much cheaper gas station 90 miles away.
    He already has 12 gallons of gas in his tank.
    How many more gallons does the truck driver need to put in his semi to make it to the cheaper gas station?"""
    
    # Define the fuel efficiency of the truck
    fuel_efficiency = 3  # miles per gallon

    # Define the distance to the cheaper gas station
    distance = 90  # miles

    # Calculate the remaining distance the truck can travel with the gas in the tank
    remaining_distance = fuel_efficiency * 12  # miles

    # Calculate the distance the truck still needs to travel
    remaining_distance -= distance

    # Calculate the additional amount of gas needed to travel the remaining distance
    additional_gas = remaining_distance / fuel_efficiency

    # return the result
    result = additional_gas
    return result

print(solution())