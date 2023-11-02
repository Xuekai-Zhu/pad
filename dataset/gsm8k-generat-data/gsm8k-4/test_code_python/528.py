def solution():
    """James buys 3 dirt bikes for $150 each and 4 off-road vehicles for $300 each. It also cost him $25 to register each of these. How much did he pay for everything?"""
    # Define the number of dirt bikes and off-road vehicles purchased, and the registration cost
    num_dirt_bikes = 3
    dirt_bike_price = 150
    num_off_road_vehicles = 4
    off_road_vehicle_price = 300
    registration_cost = 25

    # Calculate the total cost of the dirt bikes, the off-road vehicles, and the registration fees
    total_dirt_bike_cost = num_dirt_bikes * dirt_bike_price
    total_off_road_vehicle_cost = num_off_road_vehicles * off_road_vehicle_price
    total_registration_cost = (num_dirt_bikes + num_off_road_vehicles) * registration_cost

    # Calculate the total cost of everything
    total_cost = total_dirt_bike_cost + total_off_road_vehicle_cost + total_registration_cost

    result = total_cost
    return result

print(solution())