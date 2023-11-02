def solution():
    """A truck driver’s heavy semi truck can go 3 miles per gallon of gas. The truck driver needs to put gas in his truck at one gas station, but wants to put the minimum amount he needs to get him to a much cheaper gas station 90 miles away. He already has 12 gallons of gas in his tank. How many more gallons does the truck driver need to put in his semi to make it to the cheaper gas station?"""
    mpg = 3
    current_gas = 12
    distance_to_drive = 90
    gas_needed = (distance_to_drive / mpg) - current_gas
    result = gas_needed
    return result

print(solution())