def solution():
    num_lanes = 4
    trucks_per_lane = 60

    # Calculate the number of cars per lane
    cars_per_lane = trucks_per_lane * 2

    # Calculate the total number of vehicles per lane
    total_vehicles_per_lane = cars_per_lane + trucks_per_lane

    # Calculate the total number of vehicles in all the lanes
    total_vehicles = total_vehicles_per_lane * num_lanes
    result = total_vehicles
    return result

print(solution())