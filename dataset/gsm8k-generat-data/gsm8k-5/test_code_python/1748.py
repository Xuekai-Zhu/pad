def solution():
    total_vehicles = 60  # Jeff has a total of 60 matchbox cars and trucks combined
    ratio_cars_to_trucks = 2  # Jeff has twice as many cars as trucks

    # Set up the equation based on the given information
    # Let x be the number of trucks Jeff has
    # Then the number of cars he has is 2x
    # The total number of vehicles is x + 2x = 3x
    # So 3x = 60, and x = 20
    number_of_trucks = total_vehicles / (ratio_cars_to_trucks + 1)
    result = number_of_trucks
    return result

print(solution())