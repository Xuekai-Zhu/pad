def solution():
    cost_per_dirt_bike = 150  # James buys 3 dirt bikes for $150 each
    cost_per_offroad_vehicle = 300  # James buys 4 off-road vehicles for $300 each
    registration_cost = 25  # It costs $25 to register each vehicle

    # Calculate the total cost of the dirt bikes
    dirt_bike_cost = 3 * cost_per_dirt_bike
    dirt_bike_reg_cost = 3 * registration_cost
    total_dirt_bike_cost = dirt_bike_cost + dirt_bike_reg_cost

    # Calculate the total cost of the off-road vehicles
    offroad_vehicle_cost = 4 * cost_per_offroad_vehicle
    offroad_vehicle_reg_cost = 4 * registration_cost
    total_offroad_vehicle_cost = offroad_vehicle_cost + offroad_vehicle_reg_cost

    # Calculate the total cost of everything
    total_cost = total_dirt_bike_cost + total_offroad_vehicle_cost
    result = total_cost
    return result

print(solution())