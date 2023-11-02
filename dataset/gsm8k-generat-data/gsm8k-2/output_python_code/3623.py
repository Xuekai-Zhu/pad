def solution():
    """A truck driver’s heavy semi truck can go 3 miles per gallon of gas. The truck driver needs to put gas in his truck at one gas station, but wants to put the minimum amount he needs to get him to a much cheaper gas station 90 miles away. He already has 12 gallons of gas in his tank. How many more gallons does the truck driver need to put in his semi to make it to the cheaper gas station?"""
    mpg = 3
    distance = 90
    current_gas = 12
    remaining_distance = distance - (current_gas * mpg)
    additional_gas = remaining_distance / mpg
    result = additional_gas
    return result

print(solution())