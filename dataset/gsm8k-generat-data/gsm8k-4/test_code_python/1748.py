def solution():
    """Jeff is collecting matchbox cars. He has twice as many cars as trucks. He has 60 total vehicles. How many trucks does he have?"""
    # Define the total number of vehicles and the ratio of cars to trucks
    total_vehicles = 60
    car_to_truck_ratio = 2

    # Calculate the total number of trucks
    # Let x be the number of trucks.
    # Then the number of cars is 2x, since there are twice as many cars as trucks.
    # The total number of vehicles is x + 2x = 3x.
    # Solving for x, we get x = total_vehicles / 3.
    trucks = total_vehicles / 3

    # return the result
    result = trucks
    return result

print(solution())