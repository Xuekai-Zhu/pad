def solution():
    """James buys 3 dirt bikes for $150 each and 4 off-road vehicles for $300 each. It also cost him $25 to register each of these. How much did he pay for everything?"""
    # Define the cost of a dirt bike and an off-road vehicle, and the registration fee
    DIRT_BIKE_COST = 150
    OFF_ROAD_VEHICLE_COST = 300
    REGISTRATION_FEE = 25

    # Define the number of dirt bikes and off-road vehicles James buys
    num_dirt_bikes = 3
    num_off_road_vehicles = 4

    # Calculate the total cost of the dirt bikes, including registration fees
    dirt_bike_cost = num_dirt_bikes * (DIRT_BIKE_COST + REGISTRATION_FEE)

    # Calculate the total cost of the off-road vehicles, including registration fees
    off_road_vehicle_cost = num_off_road_vehicles * (OFF_ROAD_VEHICLE_COST + REGISTRATION_FEE)

    # Calculate the total cost of everything
    total_cost = dirt_bike_cost + off_road_vehicle_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())