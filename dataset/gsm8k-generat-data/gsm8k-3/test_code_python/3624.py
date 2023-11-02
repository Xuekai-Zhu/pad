def solution():
    """A truck driver’s heavy semi truck can go 3 miles per gallon of gas. The truck driver needs to put gas in his truck at one gas station, but wants to put the minimum amount he needs to get him to a much cheaper gas station 90 miles away. He already has 12 gallons of gas in his tank. How many more gallons does the truck driver need to put in his semi to make it to the cheaper gas station?"""
    # Define the truck's gas mileage
    GAS_MILEAGE = 3

    # Define the distance to the cheaper gas station
    DISTANCE = 90

    # Define the amount of gas already in the tank
    current_gas = 12

    # Calculate the remaining distance the truck can go with the current amount of gas
    remaining_distance = current_gas * GAS_MILEAGE

    # Calculate the additional gas needed to reach the cheaper gas station
    additional_gas = (DISTANCE - remaining_distance) / GAS_MILEAGE

    # Display the additional gas needed
    result = additional_gas
    return result

print(solution())