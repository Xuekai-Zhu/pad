def solution():
    num_lanes = 4
    num_trucks_per_lane = 60
    num_cars_per_lane = 2*num_trucks_per_lane

    # Calculate the total number of trucks in all the lanes
    total_trucks = num_lanes*num_trucks_per_lane

    # Calculate the total number of cars in all the lanes
    total_cars = num_lanes*num_cars_per_lane

    # Calculate the total number of vehicles in all the lanes
    total_vehicles = total_trucks + total_cars
    result = total_vehicles
    return result

print(solution())