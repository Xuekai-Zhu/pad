def solution():
    # Calculate the cost of the dirt bikes and off-road vehicles
    dirt_bikes_cost = 3 * 150  # James buys 3 dirt bikes for $150 each
    off_road_vehicles_cost = 4 * 300  # James buys 4 off-road vehicles for $300 each

    # Calculate the cost of registering the dirt bikes and off-road vehicles
    registration_cost = (3 + 4) * 25  # $25 to register each of the 7 vehicles

    # Calculate the total cost
    total_cost = dirt_bikes_cost + off_road_vehicles_cost + registration_cost
    result = total_cost
    return result

print(solution())