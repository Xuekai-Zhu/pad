def solution():
    num_dirt_bikes = 3
    dirt_bike_price = 150
    num_off_road_vehicles = 4
    off_road_vehicle_price = 300
    registration_cost = 25

    # Calculate the total cost of all dirt bikes
    total_dirt_bike_cost = num_dirt_bikes * dirt_bike_price

    # Calculate the total cost of all off-road vehicles
    total_off_road_vehicle_cost = num_off_road_vehicles * off_road_vehicle_price

    # Calculate the total registration cost
    total_registration_cost = (num_dirt_bikes + num_off_road_vehicles) * registration_cost

    # Calculate the total cost of everything
    total_cost = total_dirt_bike_cost + total_off_road_vehicle_cost + total_registration_cost
    result = total_cost
    return result

print(solution())