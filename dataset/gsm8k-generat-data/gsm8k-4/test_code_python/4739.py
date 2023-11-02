def solution():
    """On a highway, the total number of vehicles passing is 300. If the number of cars on the highway is twice the number of trucks, find out the total number of trucks on the highway?"""
    # Define the number of vehicles on the highway and the ratio of cars to trucks
    total_vehicles = 300
    car_to_truck_ratio = 2

    # Calculate the total number of cars and trucks
    total_cars = (2/3)*total_vehicles
    total_trucks = (1/3)*total_vehicles

    # Calculate the number of trucks using the car-to-truck ratio
    trucks_using_ratio = total_cars / car_to_truck_ratio
    trucks_only = total_trucks - trucks_using_ratio

    # return the result
    result = trucks_only
    return result

print(solution())