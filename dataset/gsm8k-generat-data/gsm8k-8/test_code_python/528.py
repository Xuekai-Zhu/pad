def solution():
    # Calculate the total cost of the dirt bikes
    dirt_bike_cost = 3 * 150
    dirt_bike_registration = 3 * 25
    total_dirt_bike_cost = dirt_bike_cost + dirt_bike_registration

    # Calculate the total cost of the off-road vehicles
    off_road_vehicle_cost = 4 * 300
    off_road_vehicle_registration = 4 * 25
    total_off_road_vehicle_cost = off_road_vehicle_cost + off_road_vehicle_registration

    # Calculate the total cost
    total_cost = total_dirt_bike_cost + total_off_road_vehicle_cost
    result = total_cost
    return result

print(solution())